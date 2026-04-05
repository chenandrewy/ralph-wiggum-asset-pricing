#!/usr/bin/env Rscript

# How to run: Rscript code/run-all.R
# Inputs: WRDS credentials via environment variables (WRDS_USERNAME, WRDS_PASSWORD).
# Outputs:
#   paper/exhibits/fig-opening.pdf      — Opening figure (AI stock market cap share, CRSP)
#   paper/exhibits/table-pd-ratios.tex  — Table 1 (P/D ratios vs singularity probability)
#   paper/exhibits/fig-transfers.pdf    — Figure 2 (P/D vs output growth and deadweight costs)

# ---- Create output directory ----
dir.create("paper/exhibits", recursive = TRUE, showWarnings = FALSE)

# ==============================================================
# EXHIBIT 0: Opening figure — AI stock market cap share (CRSP)
# ==============================================================

suppressPackageStartupMessages({
  library(DBI)
  library(RPostgres)
})

wrds_user <- Sys.getenv("WRDS_USERNAME", unset = Sys.getenv("PGUSER", unset = ""))
wrds_pass <- Sys.getenv("WRDS_PASSWORD", unset = Sys.getenv("PGPASSWORD", unset = ""))

if (wrds_user == "") {
  stop("Set WRDS_USERNAME (or PGUSER) before running this script.", call. = FALSE)
}

connect_args <- list(
  drv      = Postgres(),
  host     = "wrds-pgdata.wharton.upenn.edu",
  port     = 9737L,
  dbname   = "wrds",
  user     = wrds_user,
  sslmode  = "require"
)
if (wrds_pass != "") connect_args$password <- wrds_pass

con <- do.call(dbConnect, connect_args)

# Magnificent 7 permnos (AAPL, AMZN, GOOG, GOOGL, META, MSFT, NVDA, TSLA)
ai_permnos <- c(14593, 84788, 14542, 90319, 13407, 10107, 86580, 93436)

# Query: monthly market cap for all common stocks on major exchanges, 2015-2024
query <- sprintf("
  SELECT m.date,
         m.permno,
         ABS(m.prc) * m.shrout AS mcap
  FROM crsp.msf AS m
  INNER JOIN crsp.msenames AS n
    ON m.permno = n.permno
    AND m.date >= n.namedt
    AND m.date <= n.nameendt
  WHERE m.date >= '2015-01-01'
    AND m.date <= '2024-12-31'
    AND n.shrcd IN (10, 11)
    AND n.exchcd IN (1, 2, 3)
    AND m.prc IS NOT NULL
    AND m.shrout IS NOT NULL
    AND m.shrout > 0
")

cat("Downloading CRSP monthly data (2015-2024)...\n")
msf <- dbGetQuery(con, query)
dbDisconnect(con)
cat(sprintf("  Retrieved %d rows.\n", nrow(msf)))

msf$date <- as.Date(msf$date)
msf$is_ai <- msf$permno %in% ai_permnos

# Aggregate by month
months <- sort(unique(msf$date))
ai_share <- sapply(months, function(d) {
  sub <- msf[msf$date == d, ]
  total <- sum(sub$mcap, na.rm = TRUE)
  ai    <- sum(sub$mcap[sub$is_ai], na.rm = TRUE)
  if (total > 0) ai / total else NA
})

# Plot
pdf("paper/exhibits/fig-opening.pdf", width = 7, height = 4.5)
par(mar = c(4, 4.5, 1.5, 1), family = "serif")

plot(months, ai_share * 100, type = "l", lwd = 2.5, col = "#0072B2",
     xlab = "", ylab = "Share of total CRSP market capitalization (%)",
     las = 1, cex.lab = 1.05, cex.axis = 0.9,
     ylim = c(0, max(ai_share * 100, na.rm = TRUE) * 1.08))

# Shade area under the curve
polygon(c(months, rev(months)),
        c(ai_share * 100, rep(0, length(months))),
        col = adjustcolor("#0072B2", alpha.f = 0.12), border = NA)

# Label
last_idx <- length(months)
text(months[last_idx], ai_share[last_idx] * 100 + 1.0,
     sprintf("%.0f%%", ai_share[last_idx] * 100),
     col = "#0072B2", cex = 0.9, adj = c(1, 0))

mtext("AI stocks (Magnificent 7)", side = 3, line = 0.2, adj = 0,
      cex = 0.95, font = 2)

dev.off()
cat("Wrote paper/exhibits/fig-opening.pdf\n")

# ---- Common parameters ----
beta    <- 0.96       # discount factor
g       <- 0.02       # normal output growth rate
gamma   <- 3          # relative risk aversion
alpha   <- 0.15       # AI share of public output, pre-singularity
alpha_S <- 0.50       # AI share of public output, post-singularity

# ---- Core model functions ----
R_val <- beta * (1 + g)^(1 - gamma)
V_inf <- R_val / (1 - R_val)

V0 <- function(p) {
  (1 - p) * R_val / (1 - (1 - p) * R_val)
}

H_func <- function(share_S, share, Lambda, gam = gamma) {
  (share_S / share) * Lambda^(1 - gam)
}

pd_ratio <- function(p, H) {
  (1 - H) * V0(p) + H * V_inf
}

# ==============================================================
# EXHIBIT 1: Table — P/D ratios vs singularity probability
# ==============================================================

p_vals <- c(0, 0.01, 0.02, 0.05, 0.10)

# Panel A: Moderate displacement (singularity benefits household)
G_A   <- 5
phi_A <- 0.50
Lambda_A <- (1 - phi_A) * G_A   # = 2.5
H_A_ai  <- H_func(alpha_S, alpha, Lambda_A)
H_A_non <- H_func(1 - alpha_S, 1 - alpha, Lambda_A)

# Panel B: Severe displacement (negative singularity for household)
G_B   <- 2
phi_B <- 0.60
Lambda_B <- (1 - phi_B) * G_B   # = 0.8
H_B_ai  <- H_func(alpha_S, alpha, Lambda_B)
H_B_non <- H_func(1 - alpha_S, 1 - alpha, Lambda_B)

pd_A_ai  <- sapply(p_vals, function(p) pd_ratio(p, H_A_ai))
pd_A_non <- sapply(p_vals, function(p) pd_ratio(p, H_A_non))
pd_B_ai  <- sapply(p_vals, function(p) pd_ratio(p, H_B_ai))
pd_B_non <- sapply(p_vals, function(p) pd_ratio(p, H_B_non))

fmt <- function(x) {
  s <- sprintf("%.1f", x)
  sub("^-0\\.0$", "0.0", s)
}

# Build LaTeX table
header_cols <- paste(sprintf("$p = %s$", c("0", "0.01", "0.02", "0.05", "0.10")),
                     collapse = " & ")

tex <- c(
  "\\begin{tabular}{lccccc}",
  "\\toprule",
  paste0(" & ", header_cols, " \\\\"),
  "\\midrule",
  sprintf("\\multicolumn{6}{l}{\\textit{Panel A: Moderate displacement ($G = %g$, $\\phi = %g$, $\\Lambda = %g$)}} \\\\[4pt]",
          G_A, phi_A, Lambda_A),
  paste0("\\quad AI stocks & ", paste(fmt(pd_A_ai), collapse = " & "), " \\\\"),
  paste0("\\quad Non-AI stocks & ", paste(fmt(pd_A_non), collapse = " & "), " \\\\"),
  paste0("\\quad Spread & ", paste(fmt(pd_A_ai - pd_A_non), collapse = " & "), " \\\\[8pt]"),
  sprintf("\\multicolumn{6}{l}{\\textit{Panel B: Severe displacement ($G = %g$, $\\phi = %g$, $\\Lambda = %g$)}} \\\\[4pt]",
          G_B, phi_B, Lambda_B),
  paste0("\\quad AI stocks & ", paste(fmt(pd_B_ai), collapse = " & "), " \\\\"),
  paste0("\\quad Non-AI stocks & ", paste(fmt(pd_B_non), collapse = " & "), " \\\\"),
  paste0("\\quad Spread & ", paste(fmt(pd_B_ai - pd_B_non), collapse = " & "), " \\\\"),
  "\\bottomrule",
  "\\end{tabular}"
)

writeLines(tex, "paper/exhibits/table-pd-ratios.tex")
cat("Wrote paper/exhibits/table-pd-ratios.tex\n")

# ==============================================================
# EXHIBIT 2: Figure — P/D of AI stocks vs G, with transfers
# ==============================================================

G_range  <- seq(1.5, 20, length.out = 300)
phi_fig  <- 0.50
p_fig    <- 0.05
V0_fig   <- V0(p_fig)

# delta = 1 means no transfers (Lambda = (1-phi)*G)
# delta < 1 with full transfer (tau=1): Lambda = [1 - delta*phi]*G
delta_vals <- c(1.0, 0.9, 0.5, 0.0)
colors     <- c("black", "#D55E00", "#0072B2", "#009E73")
ltys       <- c(1, 5, 4, 2)

# Compute P/D curves
pd_curves <- lapply(delta_vals, function(delta) {
  if (delta == 1.0) {
    Lambda_vec <- (1 - phi_fig) * G_range
  } else {
    Lambda_vec <- (1 - delta * phi_fig) * G_range
  }
  H_vec <- (alpha_S / alpha) * Lambda_vec^(1 - gamma)
  (1 - H_vec) * V0_fig + H_vec * V_inf
})

# Determine y-axis range (clip to reasonable values)
y_max <- 50
y_min <- 5

pdf("paper/exhibits/fig-transfers.pdf", width = 7, height = 5)
par(mar = c(4.5, 4.5, 1.5, 1), family = "serif")

plot(NULL, xlim = c(1.5, 20), ylim = c(y_min, y_max),
     xlab = expression("Singularity output growth factor (" * italic(G) * ")"),
     ylab = "P/D ratio of AI stocks",
     las = 1, cex.lab = 1.1, cex.axis = 0.9)

for (i in seq_along(delta_vals)) {
  y_clipped <- pmin(pd_curves[[i]], y_max)
  lines(G_range, y_clipped, col = colors[i], lty = ltys[i], lwd = 2.2)
}

# Reference line at V0 (asymptote as G -> infinity)
abline(h = V0_fig, lty = 3, col = "gray50", lwd = 1)
text(18.5, V0_fig + 1.2, expression(italic(V)[0]), col = "gray50", cex = 0.85)

# Reference line at V_inf (no-risk benchmark)
abline(h = V_inf, lty = 3, col = "gray70", lwd = 1)
text(18.5, V_inf + 1.2, expression(italic(V)[infinity]), col = "gray70", cex = 0.85)

legend("topright",
       legend = c("No transfers",
                  expression(delta == 0.9),
                  expression(delta == 0.5),
                  expression("Perfect transfers (" * delta == 0 * ")")),
       col = colors, lty = ltys, lwd = 2.2, bty = "n", cex = 0.85,
       seg.len = 2.5)

dev.off()
cat("Wrote paper/exhibits/fig-transfers.pdf\n")

cat("\nAll exhibits generated successfully.\n")
