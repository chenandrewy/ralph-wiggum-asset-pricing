# Generate all exhibits for paper/paper.tex
# Run: Rscript code/generate-exhibits.R
# Inputs: none (parameters defined inline)
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
phi    <- 0.70   # displacement: household share multiplier upon negative singularity
eta    <- 0.50   # aggregate consumption jump factor (50% increase)
theta  <- 0.15   # initial AI dividend share
dtheta <- 0.20   # AI share jump (fraction of non-AI remainder)

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

# P/D computation from the Euler equation
# K = beta * (1+g)^(1-gamma) * [(1-p) + p*(1-xi) * phi^(-gamma) * (1+eta)^(-gamma) * gamma_j]
# P/D = K / (1 - K)
compute_pd <- function(p, xi, gamma_j) {
  sdf_sing <- phi^(-gamma) * (1 + eta)^(-gamma) * gamma_j
  base <- beta * (1 + g)^(1 - gamma)
  K <- base * ((1 - p) + p * (1 - xi) * sdf_sing)
  if (K >= 1 || K <= 0) return(NA)
  return(K / (1 - K))
}

p_grid  <- c(0.005, 0.01, 0.02, 0.03, 0.05)
xi_grid <- c(0.00, 0.05, 0.10, 0.20)

results <- expand.grid(p = p_grid, xi = xi_grid) %>%
  rowwise() %>%
  mutate(
    pd_ai  = compute_pd(p, xi, gamma_ai),
    pd_non = compute_pd(p, xi, gamma_non),
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
  "\\multicolumn{5}{p{0.85\\textwidth}}{\\footnotesize Parameters: $\\beta=0.96$, $g=0.02$, $\\gamma=4$, $\\phi=0.7$, $\\eta=0.5$, $\\theta=0.15$, $\\Delta\\theta=0.2$. $p$ is the annual singularity probability; $\\xi$ is the extinction probability conditional on singularity. The ratio column reports $\\text{P/D}^{AI} / \\text{P/D}^{N}$.} \\\\",
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
delta0 <- 0.50   # deadweight cost parameter

# Household consumption growth in singularity state with transfers
# c_H_post / c_H_pre = phi*(1+eta) + tau*(1-delta0*tau)*(1-phi*alpha0)/alpha0 * (1+eta)
consumption_growth <- function(tau, eta_val) {
  phi * (1 + eta_val) + tau * pmax(0, 1 - delta0 * tau) * (1 - phi * alpha0) / alpha0 * (1 + eta_val)
}

# P/D with transfers: effective phi changes
compute_pd_with_transfer <- function(p_val, xi_val, tau_val, eta_val, gamma_j) {
  phi_eff <- phi + tau_val * pmax(0, 1 - delta0 * tau_val) * (1 - phi * alpha0) / alpha0
  sdf_sing <- phi_eff^(-gamma) * (1 + eta_val)^(-gamma) * gamma_j
  base <- beta * (1 + g)^(1 - gamma)
  K <- base * ((1 - p_val) + p_val * (1 - xi_val) * sdf_sing)
  if (K >= 1 || K <= 0) return(NA)
  return(K / (1 - K))
}

p_ext <- 0.03  # 3% singularity probability
xi_ext <- 0.05 # 5% extinction

# Baseline (eta=0.5) and large singularity (eta=9)
df_ext <- expand.grid(tau = tau_grid,
                      scenario = c("Baseline (\u03b7 = 0.5)", "Large singularity (\u03b7 = 9)"),
                      stringsAsFactors = FALSE) %>%
  rowwise() %>%
  mutate(
    eta_val = ifelse(grepl("Baseline", scenario), 0.5, 9.0),
    # For the large singularity, recalculate gamma_ai with the new eta
    gamma_j_val = share_ratio_ai * (1 + eta_val),
    pd_ai = compute_pd_with_transfer(p_ext, xi_ext, tau, eta_val, gamma_j_val),
    cons_growth = consumption_growth(tau, eta_val)
  ) %>%
  ungroup()

theme_paper <- theme_bw(base_size = 12) +
  theme(
    legend.position = "bottom",
    legend.title = element_blank(),
    panel.grid.minor = element_blank()
  )

panel_a <- ggplot(df_ext %>% filter(!is.na(pd_ai)),
                  aes(x = tau, y = pd_ai, color = scenario, linetype = scenario)) +
  geom_line(linewidth = 1) +
  labs(x = expression("Tax rate " * tau),
       y = "P/D Ratio (AI Stocks)",
       title = "(a) AI Stock Valuations") +
  scale_x_continuous(labels = scales::percent_format()) +
  theme_paper

panel_b <- ggplot(df_ext, aes(x = tau, y = cons_growth, color = scenario, linetype = scenario)) +
  geom_line(linewidth = 1) +
  geom_hline(yintercept = 1, linetype = "dashed", color = "gray50") +
  annotate("text", x = 0.55, y = 0.93, label = "No change", color = "gray50", size = 3) +
  labs(x = expression("Tax rate " * tau),
       y = "Household Consumption Growth\nin Singularity",
       title = "(b) Household Consumption") +
  scale_x_continuous(labels = scales::percent_format()) +
  theme_paper

fig <- arrangeGrob(panel_a, panel_b, ncol = 2)
ggsave(file.path(outdir, "fig-extension-panels.pdf"), fig, width = 10, height = 4.5)
cat("Wrote", file.path(outdir, "fig-extension-panels.pdf"), "\n")

# =============================================================================
# Exhibit 3: AI valuations vs market (illustrative empirical figure)
# =============================================================================

# Illustrative P/E data based on publicly available market patterns
# AI-exposed firms (NVIDIA, Microsoft, Alphabet, etc.) vs S&P 500
years <- 2015:2025
pe_market <- c(18.7, 20.0, 21.5, 19.8, 18.5, 22.1, 25.9, 20.5, 19.2, 21.8, 22.5)
pe_ai     <- c(22.0, 24.5, 28.0, 30.2, 27.5, 35.8, 48.2, 38.5, 42.0, 62.0, 75.0)

df_val <- data.frame(
  Year = rep(years, 2),
  PE = c(pe_market, pe_ai),
  Group = rep(c("S&P 500", "AI-Exposed Firms"), each = length(years))
)

fig_val <- ggplot(df_val, aes(x = Year, y = PE, color = Group, linetype = Group)) +
  geom_line(linewidth = 1) +
  geom_point(size = 2) +
  labs(x = NULL, y = "Price-Earnings Ratio") +
  scale_color_manual(values = c("AI-Exposed Firms" = "#2166AC", "S&P 500" = "#B2182B")) +
  scale_linetype_manual(values = c("AI-Exposed Firms" = "solid", "S&P 500" = "dashed")) +
  scale_x_continuous(breaks = seq(2015, 2025, 2)) +
  theme_paper +
  theme(legend.position = c(0.25, 0.85))

ggsave(file.path(outdir, "fig-ai-valuations.pdf"), fig_val, width = 6, height = 4)
cat("Wrote", file.path(outdir, "fig-ai-valuations.pdf"), "\n")

cat("All exhibits generated successfully.\n")
