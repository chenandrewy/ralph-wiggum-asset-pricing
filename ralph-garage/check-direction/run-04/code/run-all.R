#!/usr/bin/env Rscript
# Generates all exhibits for paper/paper.tex
# Usage: Rscript code/run-all.R  (from repo root)
# Inputs: data/pd-ratios.csv
# Outputs: paper/exhibits/exhibit-1-pd-ratios.pdf
#          paper/exhibits/exhibit-2-pd-table.tex
#          paper/exhibits/exhibit-3-transfers.pdf

library(ggplot2)
library(patchwork)

dir.create("paper/exhibits", showWarnings = FALSE, recursive = TRUE)

# ============================================================
# Parameters
# ============================================================
beta  <- 0.96
gamma <- 5
g     <- 0.02
kappa <- 0.30
theta <- 1.0
phi   <- 0.20

psi <- beta * (1 + g)^(1 - gamma)

# ============================================================
# Model: P/D ratio in pre-singularity state
# ============================================================
#   PD_j = [(1-p)*psi + p*(1-xi)*psi*(1-kappa)^(-gamma)*lambda_j/(1-psi)]
#          / [1 - (1-p)*psi]
# where lambda_j is the dividend multiplier at singularity.
compute_pd <- function(p, xi, kap, lambda) {
  if (p == 0) return(psi / (1 - psi))
  denom <- 1 - (1 - p) * psi
  numer <- (1 - p) * psi +
    p * (1 - xi) * psi * (1 - kap)^(-gamma) * lambda / (1 - psi)
  numer / denom
}

# ============================================================
# Exhibit 1: Empirical valuation ratios
# ============================================================
dat <- read.csv("data/pd-ratios.csv")

p1 <- ggplot(dat, aes(x = year)) +
  geom_line(aes(y = ai_stocks, color = "AI Stocks"), linewidth = 1.1) +
  geom_point(aes(y = ai_stocks, color = "AI Stocks"), size = 2.2) +
  geom_line(aes(y = non_ai_stocks, color = "Non-AI Stocks"), linewidth = 1.1) +
  geom_point(aes(y = non_ai_stocks, color = "Non-AI Stocks"), size = 2.2) +
  scale_color_manual(values = c("AI Stocks" = "#2166AC",
                                "Non-AI Stocks" = "#B2182B")) +
  scale_x_continuous(breaks = seq(2015, 2025, 2)) +
  labs(x = NULL, y = "Price-Earnings Ratio", color = NULL) +
  theme_minimal(base_size = 14) +
  theme(legend.position = c(0.25, 0.85),
        legend.background = element_rect(fill = "white", color = NA),
        panel.grid.minor = element_blank())

ggsave("paper/exhibits/exhibit-1-pd-ratios.pdf", p1, width = 7, height = 5)
cat("Exhibit 1 saved.\n")

# ============================================================
# Exhibit 2: Quantitative P/D table
# ============================================================
p_vals  <- c(0, 0.01, 0.02, 0.05)
xi_vals <- c(0, 0.05, 0.20)

rows <- list()
for (p_val in p_vals) {
  for (xi_val in xi_vals) {
    if (p_val == 0 && xi_val > 0) next
    pd_a <- compute_pd(p_val, xi_val, kappa, 1 + theta)
    pd_n <- compute_pd(p_val, xi_val, kappa, 1 - phi)
    rows[[length(rows) + 1]] <- data.frame(
      p = p_val, xi = xi_val,
      pd_a = pd_a, pd_n = pd_n,
      ratio = pd_a / pd_n
    )
  }
}
tab <- do.call(rbind, rows)

sink("paper/exhibits/exhibit-2-pd-table.tex")
cat("\\begin{tabular}{cc ccc}\n")
cat("\\toprule\n")
cat("$p$ & $\\xi$ & $PD^{\\text{AI}}$ & $PD^{\\text{N}}$ & Ratio \\\\\n")
cat("\\midrule\n")
for (i in seq_len(nrow(tab))) {
  r <- tab[i, ]
  xi_str <- if (r$p == 0) "---" else sprintf("%.2f", r$xi)
  cat(sprintf("%.2f & %s & %.1f & %.1f & %.2f \\\\\n",
              r$p, xi_str, r$pd_a, r$pd_n, r$ratio))
  if (r$p == 0) cat("\\midrule\n")
}
cat("\\bottomrule\n")
cat("\\end{tabular}\n")
sink()
cat("Exhibit 2 saved.\n")

# ============================================================
# Exhibit 3: Government transfers (two-panel figure)
# ============================================================
alpha_own <- 0.30   # AI owners' share of singularity output
delta_0   <- 1.0    # deadweight cost parameter
G_base    <- 1.0    # baseline singularity growth
G_sing    <- 50     # singularity growth (Jones 2024)
p_tr      <- 0.02   # singularity probability for this exhibit
xi_tr     <- 0.05   # extinction probability for this exhibit

tau_grid <- seq(0, 0.95, by = 0.005)

build_transfer_data <- function(tau_grid, G_S, label) {
  out <- data.frame(tau = tau_grid, c_growth = NA_real_,
                    pd_a = NA_real_, case = label)
  for (i in seq_along(tau_grid)) {
    tau <- tau_grid[i]
    c_ratio <- (1 - kappa) + tau * (1 - delta_0 * tau) * alpha_own * G_S
    c_ratio <- max(c_ratio, 0.01)
    c_growth <- c_ratio * (1 + g)
    denom <- 1 - (1 - p_tr) * psi
    numer <- (1 - p_tr) * psi +
      p_tr * (1 - xi_tr) * psi * c_ratio^(-gamma) * (1 + theta) / (1 - psi)
    out$c_growth[i] <- c_growth
    out$pd_a[i]     <- numer / denom
  }
  out
}

df <- rbind(
  build_transfer_data(tau_grid, G_base, "Baseline"),
  build_transfer_data(tau_grid, G_sing, "Singularity Growth")
)
df$case <- factor(df$case, levels = c("Baseline", "Singularity Growth"))

panel_colors <- c("Baseline" = "#B2182B", "Singularity Growth" = "#2166AC")

pA <- ggplot(df, aes(x = tau, y = pd_a, color = case, linetype = case)) +
  geom_line(linewidth = 1.1) +
  scale_color_manual(values = panel_colors) +
  scale_linetype_manual(values = c("Baseline" = "solid",
                                   "Singularity Growth" = "dashed")) +
  labs(x = expression("Tax Rate " * tau),
       y = expression("P/D of AI Stocks  (" * PD^{AI} * ")"),
       title = "A. AI Stock Valuations",
       color = NULL, linetype = NULL) +
  theme_minimal(base_size = 12) +
  theme(legend.position = "bottom",
        panel.grid.minor = element_blank(),
        plot.title = element_text(face = "bold", size = 13))

pB <- ggplot(df, aes(x = tau, y = c_growth, color = case, linetype = case)) +
  geom_line(linewidth = 1.1) +
  geom_hline(yintercept = 1, linetype = "dotted", color = "gray40") +
  scale_color_manual(values = panel_colors) +
  scale_linetype_manual(values = c("Baseline" = "solid",
                                   "Singularity Growth" = "dashed")) +
  labs(x = expression("Tax Rate " * tau),
       y = "Consumption Growth at Singularity",
       title = "B. Household Welfare",
       color = NULL, linetype = NULL) +
  theme_minimal(base_size = 12) +
  theme(legend.position = "bottom",
        panel.grid.minor = element_blank(),
        plot.title = element_text(face = "bold", size = 13))

p3 <- pA + pB + plot_layout(guides = "collect") &
  theme(legend.position = "bottom")

ggsave("paper/exhibits/exhibit-3-transfers.pdf", p3, width = 10, height = 5)
cat("Exhibit 3 saved.\n")

cat("All exhibits generated.\n")
