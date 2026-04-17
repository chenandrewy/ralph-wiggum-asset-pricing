# Canonical entry point: generates all exhibits for paper/paper.tex
# Run:     Rscript code/generate-exhibits.R
# Inputs:  none (all parameters self-contained)
# Outputs: paper/exhibits/exhibit-1-ai-valuations.pdf
#          paper/exhibits/exhibit-2-pd-ratios.tex
#          paper/exhibits/exhibit-3-transfers.pdf

# ===========================================================================
# Parameters
# ===========================================================================

beta   <- 0.96   # discount factor
gamma  <- 3      # CRRA risk aversion
g      <- 0.02   # normal consumption / dividend growth
g_S    <- 0.10   # post-singularity growth (Jones 2024)
phi_A  <- 5.0    # AI dividend jump at singularity
phi_N  <- 0.3    # non-AI dividend jump at singularity
phi_c  <- 0.5    # household consumption jump (displacement)
p_base <- 0.02   # baseline singularity probability
pi_base <- 0.01  # baseline extinction probability

# ===========================================================================
# Model functions
# ===========================================================================

# Post-singularity P/D ratio (Gordon growth model)
pd_post <- function(beta, g_S, gamma) {
  x <- beta * (1 + g_S)^(1 - gamma)
  stopifnot(x < 1)  # convergence check
  x / (1 - x)
}

# Pre-singularity P/D ratio for asset j
pd_pre <- function(p, pi_ext, phi_j, phi_c, beta, g, g_S, gamma) {
  a     <- (1 - p) * beta * (1 + g)^(1 - gamma)
  rho_S <- pd_post(beta, g_S, gamma)
  S_j   <- p * (1 - pi_ext) * beta * phi_c^(-gamma) * phi_j * (1 + rho_S)
  (a + S_j) / (1 - a)
}

dir.create("paper/exhibits", recursive = TRUE, showWarnings = FALSE)

# ===========================================================================
# Exhibit 1: AI vs non-AI valuations (motivating empirical figure)
# ===========================================================================

# Approximate trailing P/E ratios based on publicly available market data,
# early 2025.  AI-Intensive: market-cap-weighted average of major AI firms
# (NVIDIA, Microsoft, Alphabet, Meta, Amazon).  Non-AI: remaining S&P 500.
pe_ai    <- 45
pe_nonai <- 18

pdf("paper/exhibits/exhibit-1-ai-valuations.pdf", width = 4.8, height = 4.2)
par(mar = c(4, 5, 1.5, 1), family = "serif", cex.axis = 1.05)

bp <- barplot(
  c(pe_ai, pe_nonai),
  names.arg = c("AI-Intensive\nStocks", "Non-AI\nStocks"),
  col  = c("#2166AC", "#B0B0B0"),
  border = NA,
  ylim = c(0, 55),
  ylab = "Trailing Price-Earnings Ratio",
  las  = 1,
  cex.names = 1.05,
  cex.lab   = 1.1
)
text(bp, c(pe_ai, pe_nonai) + 2.2,
     labels = c(pe_ai, pe_nonai), cex = 1.15, font = 2)

dev.off()
cat("Exhibit 1 written.\n")

# ===========================================================================
# Exhibit 2: P/D ratio table across singularity and extinction probabilities
# ===========================================================================

p_grid  <- c(0, 0.005, 0.01, 0.02, 0.05)
pi_grid <- c(0, 0.05, 0.10)

results <- expand.grid(p = p_grid, pi_ext = pi_grid)
results$pd_AI    <- mapply(pd_pre, results$p, results$pi_ext,
                           MoreArgs = list(phi_j = phi_A, phi_c = phi_c,
                                           beta = beta, g = g, g_S = g_S,
                                           gamma = gamma))
results$pd_nonAI <- mapply(pd_pre, results$p, results$pi_ext,
                           MoreArgs = list(phi_j = phi_N, phi_c = phi_c,
                                           beta = beta, g = g, g_S = g_S,
                                           gamma = gamma))

sink("paper/exhibits/exhibit-2-pd-ratios.tex")
cat("\\begin{tabular}{l rr rr rr}\n")
cat("\\toprule\n")
cat(" & \\multicolumn{2}{c}{$\\pi = 0$}")
cat(" & \\multicolumn{2}{c}{$\\pi = 0.05$}")
cat(" & \\multicolumn{2}{c}{$\\pi = 0.10$} \\\\\n")
cat("\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}\n")
cat("$p$ & AI & Non-AI & AI & Non-AI & AI & Non-AI \\\\\n")
cat("\\midrule\n")

for (p_val in p_grid) {
  if (p_val == 0) {
    label <- "$0$"
  } else {
    label <- sprintf("$%.1f\\%%$", p_val * 100)
  }
  cat(label)
  for (pi_val in pi_grid) {
    row <- results[results$p == p_val & results$pi_ext == pi_val, ]
    cat(sprintf(" & %.1f & %.1f", row$pd_AI, row$pd_nonAI))
  }
  cat(" \\\\\n")
}

cat("\\bottomrule\n")
cat("\\end{tabular}\n")
sink()
cat("Exhibit 2 written.\n")

# ===========================================================================
# Exhibit 3: Government transfers — two-panel figure
# ===========================================================================

omega_0  <- 3       # deadweight cost coefficient: fraction wasted = omega_0 * tau
phi_c_0  <- phi_c   # baseline displacement (no transfers)
Phi_base <- 2       # AI income / household consumption (baseline growth)
Phi_sing <- 20      # AI income / household consumption (singularity growth)

tau_grid <- seq(0, 0.36, length.out = 300)

# Household consumption ratio at singularity, as function of tau
phi_c_tau <- function(tau, Phi) {
  net <- tau * Phi * pmax(0, 1 - omega_0 * tau)
  phi_c_0 + net
}

# AI stock P/D as function of tau
pd_ai_tau <- function(tau, Phi) {
  fc <- phi_c_tau(tau, Phi)
  fa <- phi_A * (1 - tau)
  pd_pre(p = p_base, pi_ext = pi_base, phi_j = fa, phi_c = fc,
         beta = beta, g = g, g_S = g_S, gamma = gamma)
}

# Compute curves
pd_curve_base <- sapply(tau_grid, pd_ai_tau, Phi = Phi_base)
pd_curve_sing <- sapply(tau_grid, pd_ai_tau, Phi = Phi_sing)
fc_curve_base <- sapply(tau_grid, phi_c_tau, Phi = Phi_base)
fc_curve_sing <- sapply(tau_grid, phi_c_tau, Phi = Phi_sing)

pdf("paper/exhibits/exhibit-3-transfers.pdf", width = 9, height = 4.2)
par(mfrow = c(1, 2), mar = c(4.5, 5, 2.5, 1.5), family = "serif",
    cex.axis = 1.0, cex.lab = 1.1)

# --- Panel (a): AI Stock P/D vs tau ---
plot(tau_grid, pd_curve_base, type = "l", lwd = 2.5, col = "#B0B0B0",
     xlab = expression("Tax rate " * tau),
     ylab = "AI Stock Price-Dividend Ratio",
     main = "(a) AI Stock Valuations",
     ylim = c(0, max(pd_curve_base, pd_curve_sing) * 1.05),
     las = 1, cex.main = 1.1)
lines(tau_grid, pd_curve_sing, lwd = 2.5, col = "#2166AC")
legend("topright",
       legend = c("Singularity growth", "Baseline growth"),
       col = c("#2166AC", "#B0B0B0"), lwd = 2.5, bty = "n", cex = 0.95)

# --- Panel (b): Household consumption at singularity vs tau ---
plot(tau_grid, fc_curve_base, type = "l", lwd = 2.5, col = "#B0B0B0",
     xlab = expression("Tax rate " * tau),
     ylab = expression("Household consumption ratio  " * phi[c](tau)),
     main = "(b) Household Consumption at Singularity",
     ylim = c(0, max(fc_curve_sing) * 1.08),
     las = 1, cex.main = 1.1)
lines(tau_grid, fc_curve_sing, lwd = 2.5, col = "#2166AC")
abline(h = 1, lty = 2, col = "gray40", lwd = 1.2)
text(0.30, 1.12, "No displacement", cex = 0.85, col = "gray40", font = 3)
legend("topleft",
       legend = c("Singularity growth", "Baseline growth"),
       col = c("#2166AC", "#B0B0B0"), lwd = 2.5, bty = "n", cex = 0.95)

dev.off()
cat("Exhibit 3 written.\n")

cat("All exhibits generated successfully.\n")
