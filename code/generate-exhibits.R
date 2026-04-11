# Generate all exhibits for paper/paper.tex
# Run: Rscript code/generate-exhibits.R
# Inputs: Downloads S&P 500 and individual stock data from FRED
# Outputs: paper/exhibits/table-pd-ratios.tex, paper/exhibits/fig-extension-panels.pdf,
#          paper/exhibits/fig-ai-valuations.pdf

library(ggplot2)
library(dplyr)
library(tidyr)
library(gridExtra)

outdir <- "paper/exhibits"
dir.create(outdir, showWarnings = FALSE, recursive = TRUE)

# =============================================================================
# Parameters
# =============================================================================
beta   <- 0.96   # discount factor
g      <- 0.02   # consumption growth rate
gamma  <- 4      # risk aversion
phi    <- 0.50   # displacement: household share multiplier upon negative singularity (phi*(1+eta)=0.75)
eta    <- 0.50   # aggregate consumption jump factor (50% increase)
theta  <- 0.15   # initial AI dividend share
dtheta <- 0.20   # AI share jump (fraction of non-AI remainder)
phi_large <- 0.05 # severe displacement for large singularity: phi_large*(1+9)=0.5

# =============================================================================
# Exhibit 1: Table of P/D ratios
# =============================================================================

# Dividend growth factors conditional on non-extinction singularity
# AI: share goes from theta to theta + dtheta*(1-theta), and agg consumption * (1+eta)
# So dividend growth = [theta + dtheta*(1-theta)] / theta * (1+eta)
share_ratio_ai  <- (theta + dtheta * (1 - theta)) / theta
share_ratio_non <- (1 - theta - dtheta * (1 - theta)) / (1 - theta)
gamma_ai  <- share_ratio_ai * (1 + eta)
gamma_non <- share_ratio_non * (1 + eta)

# Closed-form P/D (approximate: treats post-singularity P/D as equal to pre-singularity)
compute_pd_approx <- function(p, xi, gamma_j) {
  sdf_sing <- phi^(-gamma) * (1 + eta)^(-gamma) * gamma_j
  base <- beta * (1 + g)^(1 - gamma)
  K <- base * ((1 - p) + p * (1 - xi) * sdf_sing)
  if (K >= 1 || K <= 0) return(NA)
  return(K / (1 - K))
}

# Exact P/D via backward recursion over the chain of theta values after
# successive singularities. Non-AI P/D is exact in closed form (Gamma^N is
# theta-independent), so this only matters for AI stocks.
compute_pd_ai_exact <- function(p, xi, theta0, dtheta, n_steps = 60) {
  B <- beta * (1 + g)^(1 - gamma)
  S <- phi^(-gamma) * (1 + eta)^(-gamma)

  # Build the chain of theta values after 0, 1, 2, ... singularities
  thetas <- numeric(n_steps + 1)
  thetas[1] <- theta0
  for (k in 2:(n_steps + 1)) {
    thetas[k] <- thetas[k - 1] + dtheta * (1 - thetas[k - 1])
  }

  # AI dividend growth factor at each theta
  gamma_ai_k <- (thetas + dtheta * (1 - thetas)) / thetas * (1 + eta)

  # Terminal value: at large k, theta ~ 1, closed-form is nearly exact
  gamma_ai_term <- gamma_ai_k[n_steps + 1]
  K_term <- B * ((1 - p) + p * (1 - xi) * S * gamma_ai_term)
  if (K_term >= 1 || K_term <= 0) return(NA)
  v <- K_term / (1 - K_term)

  # Backward recursion: v[k] = [B*(1-p) + B*p*(1-xi)*S*Gamma[k]*(v[k+1]+1)] / [1 - B*(1-p)]
  denom <- 1 - B * (1 - p)
  if (denom <= 0) return(NA)
  for (k in n_steps:1) {
    numer <- B * (1 - p) + B * p * (1 - xi) * S * gamma_ai_k[k] * (v + 1)
    v <- numer / denom
    if (!is.finite(v) || v < 0) return(NA)
  }
  return(v)
}

p_grid  <- c(0.001, 0.002, 0.005, 0.008, 0.01)
xi_grid <- c(0.00, 0.05, 0.10, 0.20)

results <- expand.grid(xi = xi_grid, p = p_grid) %>%
  select(p, xi) %>%
  rowwise() %>%
  mutate(
    pd_ai  = compute_pd_ai_exact(p, xi, theta, dtheta),
    pd_non = compute_pd_approx(p, xi, gamma_non),
    ratio  = pd_ai / pd_non
  ) %>%
  ungroup()

# Format table for LaTeX
format_num <- function(x) {
  ifelse(is.na(x), "---", sprintf("%.1f", x))
}

# Build LaTeX table
lines <- c(
  "\\begin{tabular}{cc ccc}",
  "\\toprule",
  " & & \\multicolumn{3}{c}{Price-Dividend Ratio} \\\\",
  "\\cmidrule(lr){3-5}",
  "$p$ & $\\xi$ & AI Stocks & Non-AI Stocks & Ratio \\\\",
  "\\midrule"
)

for (i in seq_len(nrow(results))) {
  r <- results[i, ]
  line <- sprintf("%.1f\\%% & %.0f\\%% & %s & %s & %s \\\\",
                  r$p * 100, r$xi * 100,
                  format_num(r$pd_ai), format_num(r$pd_non), format_num(r$ratio))
  lines <- c(lines, line)
  # Add midrule between p groups
  if (i < nrow(results) && results$p[i + 1] != results$p[i]) {
    lines <- c(lines, "\\midrule")
  }
}

lines <- c(lines,
  "\\bottomrule",
  "\\multicolumn{5}{p{0.85\\textwidth}}{\\footnotesize Parameters: $\\beta=0.96$, $g=0.02$, $\\gamma=4$, $\\phi=0.5$, $\\eta=0.5$, $\\theta=0.15$, $\\Delta\\theta=0.2$. $p$ is the annual singularity probability; $\\xi$ is the extinction probability conditional on singularity. AI P/D ratios are numerically exact, computed by iterating the Euler equation over post-singularity states (see Appendix~A). The ratio column reports $\\text{P/D}^{AI} / \\text{P/D}^{N}$.} \\\\",
  "\\end{tabular}"
)

writeLines(lines, file.path(outdir, "table-pd-ratios.tex"))
cat("Wrote", file.path(outdir, "table-pd-ratios.tex"), "\n")

# =============================================================================
# Exhibit 2: Extension figure (two panels)
# =============================================================================

# Panel A: AI stock P/D vs tax rate
# Panel B: Household consumption growth in singularity vs tax rate

tau_grid <- seq(0, 0.70, by = 0.01)

alpha0 <- 0.70   # household's initial consumption share
delta <- 0.50   # deadweight cost parameter

# Household consumption growth in singularity state with transfers
# c_H_post / c_H_pre = phi_val*(1+eta) + tau*(1-delta*tau)*(1-phi_val*alpha0)/alpha0 * (1+eta)
consumption_growth <- function(tau, eta_val, phi_val) {
  phi_val * (1 + eta_val) + tau * pmax(0, 1 - delta * tau) * (1 - phi_val * alpha0) / alpha0 * (1 + eta_val)
}

# Exact P/D with transfers via backward recursion over the theta chain.
# Mirrors compute_pd_ai_exact but uses phi_eff (incorporating transfers) in the SDF.
compute_pd_with_transfer <- function(p_val, xi_val, tau_val, eta_val, phi_val, n_steps = 60) {
  phi_eff <- phi_val + tau_val * pmax(0, 1 - delta * tau_val) * (1 - phi_val * alpha0) / alpha0
  B <- beta * (1 + g)^(1 - gamma)
  S <- phi_eff^(-gamma) * (1 + eta_val)^(-gamma)

  # Build the chain of theta values after 0, 1, 2, ... singularities
  thetas <- numeric(n_steps + 1)
  thetas[1] <- theta
  for (k in 2:(n_steps + 1)) {
    thetas[k] <- thetas[k - 1] + dtheta * (1 - thetas[k - 1])
  }

  # AI dividend growth factor at each theta
  gamma_ai_k <- (thetas + dtheta * (1 - thetas)) / thetas * (1 + eta_val)

  # Terminal value: at large k, theta ~ 1, closed-form is nearly exact
  gamma_ai_term <- gamma_ai_k[n_steps + 1]
  K_term <- B * ((1 - p_val) + p_val * (1 - xi_val) * S * gamma_ai_term)
  if (K_term >= 1 || K_term <= 0) return(NA)
  v <- K_term / (1 - K_term)

  # Backward recursion
  denom <- 1 - B * (1 - p_val)
  if (denom <= 0) return(NA)
  for (k in n_steps:1) {
    numer <- B * (1 - p_val) + B * p_val * (1 - xi_val) * S * gamma_ai_k[k] * (v + 1)
    v <- numer / denom
    if (!is.finite(v) || v < 0) return(NA)
  }
  return(v)
}

p_ext <- 0.005  # 0.5% singularity probability
xi_ext <- 0.05 # 5% extinction

# Baseline (eta=0.5, phi=0.5) and large singularity (eta=9, phi=0.05)
df_ext <- expand.grid(tau = tau_grid,
                      scenario = c("Baseline", "Large singularity"),
                      stringsAsFactors = FALSE) %>%
  rowwise() %>%
  mutate(
    eta_val = ifelse(grepl("Baseline", scenario), 0.5, 9.0),
    phi_val = ifelse(grepl("Baseline", scenario), phi, phi_large),
    pd_ai = compute_pd_with_transfer(p_ext, xi_ext, tau, eta_val, phi_val),
    cons_growth = consumption_growth(tau, eta_val, phi_val)
  ) %>%
  ungroup()

theme_paper <- theme_bw(base_size = 22) +
  theme(
    legend.position = "bottom",
    legend.title = element_blank(),
    legend.text = element_text(size = 18),
    axis.text = element_text(size = 18),
    axis.title = element_text(size = 20),
    plot.title = element_text(size = 21),
    panel.grid.minor = element_blank(),
    panel.grid.major = element_line(color = "gray75")
  )

scenario_labels <- c(
  "Baseline" = expression("Baseline (" * eta * " = 0.5, " * phi * " = 0.5)"),
  "Large singularity" = expression("Large singularity (" * eta * " = 9, " * phi * " = 0.05)")
)

# Line styles: solid vs longdash with different widths for Panel (a) differentiation
scenario_linetypes <- c("Baseline" = "solid", "Large singularity" = "longdash")
scenario_linewidths <- c("Baseline" = 1.0, "Large singularity" = 1.4)

# Darker, more saturated colors for better contrast
scenario_colors <- c("Baseline" = "#B22222", "Large singularity" = "#1B4F99")

# Compute y-axis bounds for Panel A: tighten to data range
pd_data_a <- df_ext %>% filter(!is.na(pd_ai) & tau <= 0.40)
y_min_a <- 7
baseline_max_a <- max(pd_data_a$pd_ai[pd_data_a$scenario == "Baseline"], na.rm = TRUE)
y_cap_a <- ceiling(baseline_max_a)

# Find the tau value where the large-singularity line exits the capped region
large_sing_data <- pd_data_a %>% filter(scenario == "Large singularity")
exit_tau <- large_sing_data %>% filter(pd_ai <= y_cap_a) %>% pull(tau) %>% min()

panel_a <- ggplot(pd_data_a,
                  aes(x = tau, y = pd_ai, color = scenario, linetype = scenario)) +
  geom_line(aes(linewidth = scenario)) +
  labs(x = expression("Tax rate " * tau),
       y = "P/D Ratio (AI Stocks)",
       title = "(a) AI Stock Valuations") +
  scale_x_continuous(labels = scales::percent_format(), limits = c(0, 0.40)) +
  scale_y_continuous(limits = c(y_min_a, y_cap_a)) +
  annotate("label", x = exit_tau + 0.01, y = y_cap_a * 0.95,
           label = expression(P/D %->% infinity ~ "as" ~ tau %->% 0),
           color = "#1B4F99", size = 5, hjust = 0, fontface = "bold",
           fill = "white") +
  scale_color_manual(values = scenario_colors, labels = scenario_labels) +
  scale_linetype_manual(values = scenario_linetypes, labels = scenario_labels) +
  scale_linewidth_manual(values = scenario_linewidths, labels = scenario_labels) +
  guides(linewidth = "none") +
  theme_paper

# Consumption growth at tau=0 for annotation
cons_base_0 <- consumption_growth(0, 0.5, phi)
cons_large_0 <- consumption_growth(0, 9.0, phi_large)

panel_b <- ggplot(df_ext, aes(x = tau, y = cons_growth, color = scenario, linetype = scenario)) +
  geom_line(aes(linewidth = scenario)) +
  geom_hline(yintercept = 1, linetype = "dashed", color = "black", linewidth = 2.0) +
  # Catastrophe markers at tau=0
  annotate("point", x = 0, y = cons_large_0, shape = 16, size = 3, color = "#1B4F99") +
  annotate("text", x = 0.06, y = cons_large_0 * 0.65,
           label = paste0("Catastrophe:\n", round((1 - cons_large_0) * 100), "% loss"),
           color = "#1B4F99", size = 3.5, hjust = 0, fontface = "bold") +
  annotate("point", x = 0, y = cons_base_0, shape = 16, size = 3, color = "#B22222") +
  annotate("text", x = 0.06, y = cons_base_0 * 0.75,
           label = paste0(round((1 - cons_base_0) * 100), "% loss"),
           color = "#B22222", size = 3.2, hjust = 0) +
  annotate("text", x = 0.42, y = 1.15, label = "No change", color = "black", size = 4.5, fontface = "bold") +
  labs(x = expression("Tax rate " * tau),
       y = "Household Consumption Growth\nin Singularity",
       title = "(b) Household Consumption") +
  scale_x_continuous(labels = scales::percent_format(), limits = c(0, 0.50)) +
  scale_y_log10(breaks = c(0.1, 0.25, 0.5, 1, 2, 5)) +
  scale_color_manual(values = scenario_colors, labels = scenario_labels) +
  scale_linetype_manual(values = scenario_linetypes, labels = scenario_labels) +
  scale_linewidth_manual(values = scenario_linewidths, labels = scenario_labels) +
  guides(linewidth = "none") +
  theme_paper

# Extract shared legend from panel_a, then remove legends from both panels
get_legend <- function(p) {
  tmp <- ggplotGrob(p)
  leg <- which(sapply(tmp$grobs, function(x) x$name) == "guide-box")
  tmp$grobs[[leg]]
}
shared_legend <- get_legend(panel_a)
panel_a <- panel_a + theme(legend.position = "none")
panel_b <- panel_b + theme(legend.position = "none")

fig <- arrangeGrob(
  arrangeGrob(panel_a, panel_b, ncol = 2),
  shared_legend,
  nrow = 2, heights = c(10, 1)
)
ggsave(file.path(outdir, "fig-extension-panels.pdf"), fig, width = 12, height = 7)
cat("Wrote", file.path(outdir, "fig-extension-panels.pdf"), "\n")

# =============================================================================
# Exhibit 3: Valuation ratios — S&P 500 P/D from Shiller data
# =============================================================================

# Download Shiller dataset with price, dividend, and PE10 (CAPE)
cat("Downloading S&P 500 data from datahub (Shiller dataset)...\n")
sp500_raw <- read.csv("https://datahub.io/core/s-and-p-500/r/data.csv",
                       stringsAsFactors = FALSE)
sp500_raw$Date <- as.Date(sp500_raw$Date)

# Compute trailing 12-month P/D ratio
sp500_val <- sp500_raw %>%
  filter(!is.na(SP500), !is.na(Dividend), Dividend > 0) %>%
  mutate(PD = SP500 / Dividend) %>%
  filter(Date >= as.Date("1990-01-01"), Date <= as.Date("2025-12-31"))

# PE10 (Shiller CAPE) is also available
sp500_val <- sp500_val %>% filter(!is.na(PE10), PE10 > 0)

# Download NASDAQ from FRED for the price ratio
download_fred <- function(series_id, start = "1990-01-01", end = "2025-12-31") {
  url <- sprintf(
    "https://fred.stlouisfed.org/graph/fredgraph.csv?id=%s&cosd=%s&coed=%s&fq=Monthly",
    series_id, start, end
  )
  tmp <- tempfile(fileext = ".csv")
  download.file(url, tmp, method = "libcurl", quiet = TRUE)
  d <- read.csv(tmp, stringsAsFactors = FALSE)
  names(d) <- c("Date", "Value")
  d$Date <- as.Date(d$Date)
  d$Value <- as.numeric(d$Value)
  d <- d[!is.na(d$Value), ]
  d
}

cat("Downloading NASDAQ data from FRED...\n")
nasdaq <- download_fred("NASDAQCOM")

# Aggregate to monthly (take last observation per month)
to_monthly <- function(d) {
  d$YM <- format(d$Date, "%Y-%m")
  d %>% group_by(YM) %>% slice_tail(n = 1) %>% ungroup() %>%
    select(Date, Value)
}

nasdaq_m <- to_monthly(nasdaq)
sp500_m <- sp500_val %>% select(Date, Value = SP500) %>% to_monthly()

# Compute NASDAQ/S&P price ratio as a measure of relative valuation
min_date <- max(min(sp500_m$Date), min(nasdaq_m$Date))
max_date <- min(max(sp500_m$Date), max(nasdaq_m$Date))
sp500_m  <- sp500_m  %>% filter(Date >= min_date, Date <= max_date)
nasdaq_m <- nasdaq_m %>% filter(Date >= min_date, Date <= max_date)

# Merge and compute ratio
price_ratio <- inner_join(
  sp500_m %>% rename(SP500 = Value),
  nasdaq_m %>% rename(NASDAQ = Value),
  by = "Date"
) %>%
  mutate(Ratio = NASDAQ / SP500)

# Get S&P 500 P/D for joined dates (aggregate to monthly)
sp500_pd <- sp500_val %>%
  select(Date, PD, PE10) %>%
  mutate(YM = format(Date, "%Y-%m")) %>%
  group_by(YM) %>% slice_tail(n = 1) %>% ungroup() %>%
  select(Date, PD, PE10)

# Two-panel figure: Panel (a) S&P 500 P/D ratio over time, Panel (b) NASDAQ/S&P price ratio
df_pd <- sp500_pd %>%
  inner_join(price_ratio %>% select(Date, Ratio), by = "Date") %>%
  filter(Date >= as.Date("2000-01-01"))

panel_val_a <- ggplot(df_pd, aes(x = Date, y = PD)) +
  geom_line(linewidth = 1, color = "#B2182B") +
  labs(x = NULL, y = "Price / Trailing Dividend") +
  scale_x_date(date_breaks = "5 years", date_labels = "%Y") +
  scale_y_continuous(expand = expansion(mult = c(0.02, 0.05))) +
  ggtitle("(a) S&P 500 P/D Ratio") +
  theme_paper +
  theme(plot.margin = margin(t = 10, r = 10, b = 5, l = 10, unit = "pt"),
        panel.grid.major = element_blank())

# Normalize NASDAQ/S&P ratio to Jan 2015 = 100
base_ratio <- df_pd$Ratio[which.min(abs(df_pd$Date - as.Date("2015-01-01")))]
df_pd$Ratio_norm <- df_pd$Ratio / base_ratio * 100

panel_val_b <- ggplot(df_pd, aes(x = Date, y = Ratio_norm)) +
  geom_line(linewidth = 1, color = "#2166AC") +
  geom_hline(yintercept = 100, linetype = "dashed", color = "gray50") +
  labs(x = NULL, y = "NASDAQ / S&P 500 Price Ratio\n(Jan 2015 = 100)") +
  scale_x_date(date_breaks = "5 years", date_labels = "%Y") +
  scale_y_continuous(expand = expansion(mult = c(0.02, 0.05))) +
  ggtitle("(b) Relative Valuation: NASDAQ vs. S&P 500") +
  theme_paper +
  theme(plot.margin = margin(t = 10, r = 10, b = 5, l = 10, unit = "pt"),
        panel.grid.major = element_blank())

fig_val <- arrangeGrob(panel_val_a, panel_val_b, ncol = 2)
ggsave(file.path(outdir, "fig-ai-valuations.pdf"), fig_val, width = 12, height = 4.5)
cat("Wrote", file.path(outdir, "fig-ai-valuations.pdf"), "\n")

# =============================================================================
# Veto example computation (printed to console, referenced in-text in Section 4.1)
# =============================================================================

# Infinite-horizon expected utility: develop AI vs veto.
# Bellman equation with CRRA homogeneity. Extinction utility normalized to 0.

gamma_veto  <- 10
p_veto      <- 0.01   # 1% annual singularity probability
prob_pos_v  <- 0.70
prob_neg_v  <- 0.30
kappa_veto  <- 0.01   # 1% permanent consumption loss from veto
alpha_veto  <- 0.70

u_crra <- function(c, gam) c^(1 - gam) / (1 - gam)
pv_factor <- function(gam) 1 / (1 - beta * (1 + g)^(1 - gam))

# V = u(alpha) + B*[(1-p)*V + p*(1-xi)*(q*V_pos + (1-q)*V_neg) + p*xi*0]
# where V_pos/V_neg are PV of deterministic post-singularity streams.
compute_v_develop_veto <- function(gam, p_val) {
  B <- beta * (1 + g)^(1 - gam)
  alpha_pos <- min(1, alpha_veto / phi)
  alpha_neg <- phi * alpha_veto
  pv <- pv_factor(gam)
  v_post_pos <- u_crra(alpha_pos * (1 + eta), gam) * pv
  v_post_neg <- u_crra(alpha_neg * (1 + eta), gam) * pv
  denom <- 1 - B * (1 - p_val)
  if (denom <= 0) return(NA)
  sing_val <- p_val * (1 - xi_ext) * (prob_pos_v * v_post_pos + prob_neg_v * v_post_neg)
  (u_crra(alpha_veto, gam) + B * sing_val) / denom
}

compute_v_veto <- function(gam) {
  u_crra(alpha_veto * (1 - kappa_veto), gam) * pv_factor(gam)
}

compute_v_develop_complete_veto <- function(gam, p_val) {
  B <- beta * (1 + g)^(1 - gam)
  pv <- pv_factor(gam)
  v_post <- u_crra(alpha_veto * (1 + eta), gam) * pv
  denom <- 1 - B * (1 - p_val)
  if (denom <= 0) return(NA)
  (u_crra(alpha_veto, gam) + B * p_val * (1 - xi_ext) * v_post) / denom
}

v_dev  <- compute_v_develop_veto(gamma_veto, p_veto)
v_vet  <- compute_v_veto(gamma_veto)
v_comp <- compute_v_develop_complete_veto(gamma_veto, p_veto)

cat("\n=== Veto Example (Section 4.1) ===\n")
cat(sprintf("gamma=%d, p=%.0f%%, kappa=%.0f%%, phi=%.1f, eta=%.1f, xi=%.0f%%\n",
            gamma_veto, p_veto*100, kappa_veto*100, phi, eta, xi_ext*100))
cat(sprintf("Positive singularity prob (cond. non-ext): %.0f%%\n", prob_pos_v*100))
cat(sprintf("Incomplete markets: V_develop=%.4f, V_veto=%.4f => %s\n",
            v_dev, v_vet, ifelse(v_vet > v_dev, "VETO", "develop")))
cat(sprintf("Complete markets:   V_develop=%.4f, V_veto=%.4f => %s\n",
            v_comp, v_vet, ifelse(v_vet > v_comp, "VETO", "develop")))

cat("\nAll exhibits generated successfully.\n")
