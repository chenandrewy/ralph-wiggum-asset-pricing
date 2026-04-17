# run_all.R — Canonical entry point for all exhibits
# Usage: Rscript code/run_all.R
# Inputs: none (all data generated internally; empirical figure uses illustrative data)
# Outputs: paper/exhibits/fig_intro_valuations.pdf
#          paper/exhibits/tab_pd_ratios.tex
#          paper/exhibits/fig_transfers_pd.pdf
#          paper/exhibits/fig_transfers_cons.pdf

library(ggplot2)
library(dplyr)
library(tidyr)

out_dir <- "paper/exhibits"
dir.create(out_dir, showWarnings = FALSE, recursive = TRUE)

# ============================================================
# Color palette
# ============================================================
col_ai    <- "#E63946"
col_nonai <- "#457B9D"
col_mod   <- "#E76F51"
col_large <- "#264653"

# ============================================================
# Exhibit 1: Empirical AI vs non-AI valuation ratios (intro)
# ============================================================
# Illustrative data based on public market P/E patterns.
# AI-exposed: firms in top quintile of AI revenue/patent exposure.
# Uses stylized but realistic magnitudes from 2015-2024.

years <- 2015:2024
pe_ai    <- c(28, 30, 35, 40, 38, 45, 55, 50, 65, 75)
pe_nonai <- c(18, 19, 20, 21, 20, 22, 23, 22, 24, 25)

df_pe <- data.frame(
  Year = rep(years, 2),
  PE   = c(pe_ai, pe_nonai),
  Group = rep(c("AI-exposed stocks", "Other stocks"), each = length(years))
)

p1 <- ggplot(df_pe, aes(x = Year, y = PE, color = Group, linetype = Group)) +
  geom_line(linewidth = 1.2) +
  geom_point(size = 2.5) +
  scale_color_manual(values = c("AI-exposed stocks" = col_ai,
                                "Other stocks" = col_nonai)) +
  scale_linetype_manual(values = c("AI-exposed stocks" = "solid",
                                   "Other stocks" = "dashed")) +
  labs(x = NULL, y = "Price / Earnings", color = NULL, linetype = NULL) +
  theme_minimal(base_size = 14) +
  theme(
    legend.position = c(0.25, 0.85),
    legend.background = element_rect(fill = "white", color = NA),
    panel.grid.minor = element_blank()
  ) +
  scale_x_continuous(breaks = seq(2015, 2024, 2))

ggsave(file.path(out_dir, "fig_intro_valuations.pdf"), p1, width = 7, height = 4.5)
cat("Wrote fig_intro_valuations.pdf\n")

# ============================================================
# Model functions
# ============================================================

compute_pd <- function(p, q, beta, gamma, g, G,
                       phi, phi_bar, psi, eta, eta_bar) {
  # Household consumption growth: c_{t+1}/c_t
  # Normal state: (1+g)
  # Singularity state: G * (1 - eta_bar) / (1 - eta)
  #   (household gets labor income + all public dividends)
  cs_ratio <- G * (1 - eta_bar) / (1 - eta)

  # SDF-weighted dividend growth in normal state (same for both assets)
  M <- beta * (1 + g)^(1 - gamma)

  # SDF-weighted dividend growth in singularity state
  sdf_sing <- beta * cs_ratio^(-gamma)
  Lambda_AI <- sdf_sing * G * phi_bar / phi
  Lambda_N  <- sdf_sing * G  # psi unchanged

  # P/D ratios: v = numerator / (1 - numerator)
  num_AI <- (1 - p) * M + p * (1 - q) * Lambda_AI
  num_N  <- (1 - p) * M + p * (1 - q) * Lambda_N

  v_AI <- num_AI / (1 - num_AI)
  v_N  <- num_N / (1 - num_N)

  list(v_AI = v_AI, v_N = v_N, hh_cons_growth = cs_ratio)
}

# ============================================================
# Exhibit 2: Table of P/D ratios (baseline model)
# ============================================================

# Baseline parameters
beta <- 0.96; gamma <- 3; g <- 0.02; G <- 3
phi <- 0.05; phi_bar <- 0.20; psi <- 0.25
eta <- 0.10; eta_bar <- 0.40

p_vals <- c(0.005, 0.01, 0.02, 0.05, 0.10)
q_vals <- c(0, 0.05, 0.10)

results <- expand.grid(p = p_vals, q = q_vals)
results$v_AI <- NA
results$v_N  <- NA

for (i in seq_len(nrow(results))) {
  res <- compute_pd(results$p[i], results$q[i],
                    beta, gamma, g, G,
                    phi, phi_bar, psi, eta, eta_bar)
  results$v_AI[i] <- res$v_AI
  results$v_N[i]  <- res$v_N
}

# Format table for LaTeX
tab_wide <- results %>%
  mutate(
    v_AI = round(v_AI, 1),
    v_N  = round(v_N, 1)
  ) %>%
  pivot_wider(
    id_cols = p,
    names_from = q,
    values_from = c(v_AI, v_N),
    names_glue = "{.value}_q{q}"
  ) %>%
  select(p, v_AI_q0, v_N_q0, v_AI_q0.05, v_N_q0.05, v_AI_q0.1, v_N_q0.1)

tex_lines <- c(
  "\\begin{tabular}{c cc cc cc}",
  "\\toprule",
  " & \\multicolumn{2}{c}{$q = 0$} & \\multicolumn{2}{c}{$q = 0.05$} & \\multicolumn{2}{c}{$q = 0.10$} \\\\",
  "\\cmidrule(lr){2-3} \\cmidrule(lr){4-5} \\cmidrule(lr){6-7}",
  "$p$ & AI & Non-AI & AI & Non-AI & AI & Non-AI \\\\"
)
tex_lines <- c(tex_lines, "\\midrule")

for (i in seq_len(nrow(tab_wide))) {
  row <- tab_wide[i, ]
  line <- sprintf("%.1f\\%% & %.1f & %.1f & %.1f & %.1f & %.1f & %.1f \\\\",
                  row$p * 100,
                  row$v_AI_q0, row$v_N_q0,
                  row$v_AI_q0.05, row$v_N_q0.05,
                  row$v_AI_q0.1, row$v_N_q0.1)
  tex_lines <- c(tex_lines, line)
}

tex_lines <- c(tex_lines, "\\bottomrule", "\\end{tabular}")
writeLines(tex_lines, file.path(out_dir, "tab_pd_ratios.tex"))
cat("Wrote tab_pd_ratios.tex\n")

# ============================================================
# Exhibit 3: Government transfers (two-panel figure)
#
# Uses a STRONGER displacement parameterization than the baseline
# table, so that the singularity is catastrophic for the household
# absent transfers (c_s/c < 1 for moderate G).
# ============================================================

# Extension parameters (branching off baseline)
eta_ext     <- 0.10
eta_bar_ext <- 0.80   # severe: 80% of economy goes to private AI capital
phi_ext     <- 0.05
phi_bar_ext <- 0.06   # minimal public AI share growth (most AI value is private)
psi_ext     <- 0.25
delta_waste <- 0.8    # deadweight cost parameter
p_ext       <- 0.005  # low singularity probability (model stability)
q_ext       <- 0.05
gamma_ext   <- 3
beta_ext    <- 0.96
g_ext       <- 0.02

compute_transfer_effects <- function(tau, G_val,
                                     beta, gamma, g, p, q,
                                     phi, phi_bar, psi,
                                     eta, eta_bar, delta_waste) {
  # Transfer efficiency: fraction of collected tax revenue reaching household
  theta <- pmax(1 - delta_waste * tau, 0)

  # Household share of output in singularity with transfers:
  # (1 - eta_bar) from labor + public dividends, plus transfer
  hh_share_sing <- (1 - eta_bar) + tau * theta * eta_bar

  # Consumption growth in singularity
  cs_ratio <- G_val * hh_share_sing / (1 - eta)

  # SDF in singularity
  sdf_sing <- beta * cs_ratio^(-gamma)

  # P/D for AI stocks
  M <- beta * (1 + g)^(1 - gamma)
  Lambda_AI <- sdf_sing * G_val * phi_bar / phi

  num_AI <- (1 - p) * M + p * (1 - q) * Lambda_AI

  # Guard against explosive prices (num >= 1)
  if (num_AI >= 1) {
    v_AI <- NA
  } else {
    v_AI <- num_AI / (1 - num_AI)
  }

  list(v_AI = v_AI, hh_cons_growth = cs_ratio)
}

tau_grid   <- seq(0, 0.60, by = 0.005)
G_moderate <- 3
G_large    <- 50

df_transfers <- data.frame()

for (G_val in c(G_moderate, G_large)) {
  G_label <- ifelse(G_val == G_moderate,
                    paste0("Moderate (G = ", G_moderate, ")"),
                    paste0("Large (G = ", G_large, ")"))
  for (tau in tau_grid) {
    res <- compute_transfer_effects(
      tau, G_val,
      beta_ext, gamma_ext, g_ext, p_ext, q_ext,
      phi_ext, phi_bar_ext, psi_ext,
      eta_ext, eta_bar_ext, delta_waste
    )
    df_transfers <- rbind(df_transfers, data.frame(
      tau = tau,
      v_AI = res$v_AI,
      hh_cons_growth = res$hh_cons_growth,
      Scenario = G_label
    ))
  }
}

# Panel A: P/D of AI stocks vs tau
p2a <- ggplot(df_transfers %>% filter(!is.na(v_AI)),
              aes(x = tau, y = v_AI, color = Scenario, linetype = Scenario)) +
  geom_line(linewidth = 1.2) +
  scale_color_manual(values = c(
    setNames(col_mod, paste0("Moderate (G = ", G_moderate, ")")),
    setNames(col_large, paste0("Large (G = ", G_large, ")"))
  )) +
  scale_linetype_manual(values = c(
    setNames("dashed", paste0("Moderate (G = ", G_moderate, ")")),
    setNames("solid", paste0("Large (G = ", G_large, ")"))
  )) +
  labs(
    x = expression("Tax rate " * tau),
    y = "Price / Dividend (AI stocks)",
    color = NULL, linetype = NULL
  ) +
  theme_minimal(base_size = 13) +
  theme(
    legend.position = c(0.70, 0.85),
    legend.background = element_rect(fill = "white", color = NA),
    panel.grid.minor = element_blank()
  )

ggsave(file.path(out_dir, "fig_transfers_pd.pdf"), p2a, width = 5.5, height = 4.5)
cat("Wrote fig_transfers_pd.pdf\n")

# Panel B: Household consumption growth in singularity vs tau (log scale)
p2b <- ggplot(df_transfers,
              aes(x = tau, y = hh_cons_growth, color = Scenario, linetype = Scenario)) +
  geom_line(linewidth = 1.2) +
  geom_hline(yintercept = 1, linetype = "dotted", color = "gray40", linewidth = 0.6) +
  annotate("text", x = 0.56, y = 1.15, label = "No change",
           color = "gray40", size = 3.5, fontface = "italic") +
  scale_y_log10(breaks = c(0.5, 1, 2, 5, 10, 25)) +
  scale_color_manual(values = c(
    setNames(col_mod, paste0("Moderate (G = ", G_moderate, ")")),
    setNames(col_large, paste0("Large (G = ", G_large, ")"))
  )) +
  scale_linetype_manual(values = c(
    setNames("dashed", paste0("Moderate (G = ", G_moderate, ")")),
    setNames("solid", paste0("Large (G = ", G_large, ")"))
  )) +
  labs(
    x = expression("Tax rate " * tau),
    y = expression(c[s]^H / c^H ~ "(log scale)"),
    color = NULL, linetype = NULL
  ) +
  theme_minimal(base_size = 13) +
  theme(
    legend.position = c(0.70, 0.25),
    legend.background = element_rect(fill = "white", color = NA),
    panel.grid.minor = element_blank()
  )

ggsave(file.path(out_dir, "fig_transfers_cons.pdf"), p2b, width = 5.5, height = 4.5)
cat("Wrote fig_transfers_cons.pdf\n")

cat("\nAll exhibits generated successfully.\n")
