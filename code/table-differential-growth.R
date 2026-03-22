# Compute differential-growth calibration table for the paper.
# Run: Rscript code/table-differential-growth.R
# Input: none (parameters hardcoded from paper)
# Output: prints LaTeX table fragment to stdout

# Baseline parameters
beta  <- 0.96
gamma <- 3
gN    <- 0.02
theta <- 0.50
phi   <- 0.30
s0    <- 0.15

# Grid
delta_g_vals <- c(0.00, 0.01, 0.02, 0.03, 0.04, 0.05)
lambda_vals  <- c(0.01, 0.02, 0.05)

# Horizon for recursion (enough for convergence)
T <- 200

compute_pd <- function(gA, gN, lambda, beta, gamma, theta, phi, s0, T) {
  # Compute time-varying s_t path
  s <- numeric(T + 1)
  s[1] <- s0
  for (t in 1:T) {
    G_t <- s[t] * (1 + gA) + (1 - s[t]) * (1 + gN)
    s[t + 1] <- s[t] * (1 + gA) / G_t
  }

  # Post-singularity P/D ratios (constant growth at gA and gN respectively)
  # After singularity, no more risk. AI stock grows at gA, non-AI at gN.
  # Post-singularity SDF depends on aggregate growth which depends on s_t at
  # the time of singularity. For the post-singularity regime, dividends grow
  # deterministically. We need post-singularity v^A and v^N at each possible
  # singularity time t.

  # Post-singularity: the economy grows deterministically.
  # At time t (post-sing), s evolves deterministically from s_t^post.
  # s_t^post after singularity at time t:
  # D^A jumps by (1+theta), D^N drops by (1-phi)
  # s_post = s_t*(1+theta)*(1+gA) / [s_t*(1+theta)*(1+gA) + (1-s_t)*(1-phi)*(1+gN)]
  # But for P/D, we need to solve the post-singularity Euler recursion backward.

  # Post-singularity: no more shocks. P/D for AI stock at time t (post-sing):
  # v_t^A = beta * (1+gA) * G_post(s_t)^{-gamma} * (1 + v_{t+1}^A)
  # where G_post(s) = s*(1+gA) + (1-s)*(1+gN)

  # Backward induction for post-singularity, starting from T
  vA_post <- numeric(T + 1)
  vN_post <- numeric(T + 1)
  s_post  <- numeric(T + 1)

  # We need post-singularity values for singularity occurring at each t
  # If singularity occurs at t, the post-singularity s starts from:
  # s_post_t = [s_t * (1+theta) * (1+gA)] / [s_t*(1+theta)*(1+gA) + (1-s_t)*(1-phi)*(1+gN)]

  # For each possible singularity time, compute post-singularity continuation
  # Actually, we just need the post-singularity v^A at t=0 for the pre-singularity recursion.
  # The pre-singularity recursion uses bar_v_{t+1}^A which is the post-singularity P/D
  # if singularity occurs at time t.

  # Let's compute post-singularity P/D for singularity at each time t
  vA_bar <- numeric(T + 1)  # post-singularity continuation for AI stock
  vN_bar <- numeric(T + 1)  # post-singularity continuation for non-AI stock

  for (sing_t in 0:T) {
    # s after singularity at time sing_t
    num_s <- s[sing_t + 1] * (1 + theta) * (1 + gA)
    den_s <- num_s + (1 - s[sing_t + 1]) * (1 - phi) * (1 + gN)
    s_p <- num_s / den_s

    n_post <- T - sing_t + 1
    s_path <- numeric(n_post)
    s_path[1] <- s_p
    if (n_post > 1) {
      for (k in 2:n_post) {
        G_k <- s_path[k-1] * (1 + gA) + (1 - s_path[k-1]) * (1 + gN)
        s_path[k] <- s_path[k-1] * (1 + gA) / G_k
      }
    }

    vA_p <- numeric(n_post)
    vN_p <- numeric(n_post)
    G_end <- s_path[n_post] * (1 + gA) + (1 - s_path[n_post]) * (1 + gN)
    aA_end <- beta * (1 + gA) * G_end^(-gamma)
    aN_end <- beta * (1 + gN) * G_end^(-gamma)
    vA_p[n_post] <- aA_end / (1 - aA_end)
    vN_p[n_post] <- aN_end / (1 - aN_end)

    if (n_post > 1) {
      for (k in (n_post - 1):1) {
        G_k <- s_path[k] * (1 + gA) + (1 - s_path[k]) * (1 + gN)
        aA_k <- beta * (1 + gA) * G_k^(-gamma)
        aN_k <- beta * (1 + gN) * G_k^(-gamma)
        vA_p[k] <- aA_k * (1 + vA_p[k + 1])
        vN_p[k] <- aN_k * (1 + vN_p[k + 1])
      }
    }

    vA_bar[sing_t + 1] <- vA_p[1]
    vN_bar[sing_t + 1] <- vN_p[1]
  }

  # Pre-singularity backward induction
  vA_pre <- numeric(T + 1)
  vN_pre <- numeric(T + 1)

  # Terminal condition
  G_T <- s[T + 1] * (1 + gA) + (1 - s[T + 1]) * (1 + gN)
  aA_T <- beta * (1 + gA) * G_T^(-gamma)
  aN_T <- beta * (1 + gN) * G_T^(-gamma)
  vA_pre[T + 1] <- aA_T / (1 - aA_T)
  vN_pre[T + 1] <- aN_T / (1 - aN_T)

  for (t in T:1) {
    G_t <- s[t] * (1 + gA) + (1 - s[t]) * (1 + gN)
    J_t <- (s[t] * (1 + theta) * (1 + gA) + (1 - s[t]) * (1 - phi) * (1 + gN)) / G_t
    aA_t <- beta * (1 + gA) * G_t^(-gamma)
    aN_t <- beta * (1 + gN) * G_t^(-gamma)

    vA_pre[t] <- (1 - lambda) * aA_t * (1 + vA_pre[t + 1]) +
                  lambda * aA_t * J_t^(-gamma) * (1 + theta) * (1 + vA_bar[t])
    vN_pre[t] <- (1 - lambda) * aN_t * (1 + vN_pre[t + 1]) +
                  lambda * aN_t * J_t^(-gamma) * (1 - phi) * (1 + vN_bar[t])
  }

  # Return t=0 values
  list(vA = vA_pre[1], vN = vN_pre[1])
}

# Also compute cash-flow-only premium (set gamma -> 0 equivalent: J^{-gamma} = 1)
compute_pd_cashflow <- function(gA, gN, lambda, beta, gamma, theta, phi, s0, T) {
  # Same recursion but with J^{-gamma} replaced by 1
  s <- numeric(T + 1)
  s[1] <- s0
  for (t in 1:T) {
    G_t <- s[t] * (1 + gA) + (1 - s[t]) * (1 + gN)
    s[t + 1] <- s[t] * (1 + gA) / G_t
  }

  vA_bar <- numeric(T + 1)
  vN_bar <- numeric(T + 1)

  for (sing_t in 0:T) {
    num_s <- s[sing_t + 1] * (1 + theta) * (1 + gA)
    den_s <- num_s + (1 - s[sing_t + 1]) * (1 - phi) * (1 + gN)
    s_p <- num_s / den_s

    n_post <- T - sing_t + 1
    s_path <- numeric(n_post)
    s_path[1] <- s_p
    if (n_post > 1) {
      for (k in 2:n_post) {
        G_k <- s_path[k-1] * (1 + gA) + (1 - s_path[k-1]) * (1 + gN)
        s_path[k] <- s_path[k-1] * (1 + gA) / G_k
      }
    }

    vA_p <- numeric(n_post)
    vN_p <- numeric(n_post)
    G_end <- s_path[n_post] * (1 + gA) + (1 - s_path[n_post]) * (1 + gN)
    aA_end <- beta * (1 + gA) * G_end^(-gamma)
    aN_end <- beta * (1 + gN) * G_end^(-gamma)
    vA_p[n_post] <- aA_end / (1 - aA_end)
    vN_p[n_post] <- aN_end / (1 - aN_end)

    if (n_post > 1) {
      for (k in (n_post - 1):1) {
        G_k <- s_path[k] * (1 + gA) + (1 - s_path[k]) * (1 + gN)
        aA_k <- beta * (1 + gA) * G_k^(-gamma)
        aN_k <- beta * (1 + gN) * G_k^(-gamma)
        vA_p[k] <- aA_k * (1 + vA_p[k + 1])
        vN_p[k] <- aN_k * (1 + vN_p[k + 1])
      }
    }

    vA_bar[sing_t + 1] <- vA_p[1]
    vN_bar[sing_t + 1] <- vN_p[1]
  }

  vA_pre <- numeric(T + 1)
  vN_pre <- numeric(T + 1)

  G_T <- s[T + 1] * (1 + gA) + (1 - s[T + 1]) * (1 + gN)
  aA_T <- beta * (1 + gA) * G_T^(-gamma)
  aN_T <- beta * (1 + gN) * G_T^(-gamma)
  vA_pre[T + 1] <- aA_T / (1 - aA_T)
  vN_pre[T + 1] <- aN_T / (1 - aN_T)

  for (t in T:1) {
    G_t <- s[t] * (1 + gA) + (1 - s[t]) * (1 + gN)
    aA_t <- beta * (1 + gA) * G_t^(-gamma)
    aN_t <- beta * (1 + gN) * G_t^(-gamma)

    # J^{-gamma} = 1 (risk-neutral pricing)
    vA_pre[t] <- (1 - lambda) * aA_t * (1 + vA_pre[t + 1]) +
                  lambda * aA_t * (1 + theta) * (1 + vA_bar[t])
    vN_pre[t] <- (1 - lambda) * aN_t * (1 + vN_pre[t + 1]) +
                  lambda * aN_t * (1 - phi) * (1 + vN_bar[t])
  }

  list(vA = vA_pre[1], vN = vN_pre[1])
}

# Build results table
results <- data.frame(
  delta_g = numeric(),
  lambda  = numeric(),
  vA      = numeric(),
  vN      = numeric(),
  ratio   = numeric(),
  cf_ratio = numeric(),
  hedge_share = numeric()
)

for (dg in delta_g_vals) {
  for (lam in lambda_vals) {
    gA <- gN + dg
    res <- compute_pd(gA, gN, lam, beta, gamma, theta, phi, s0, T)
    cf  <- compute_pd_cashflow(gA, gN, lam, beta, gamma, theta, phi, s0, T)

    total_premium <- res$vA / res$vN
    cf_premium    <- cf$vA / cf$vN

    # Hedging share: fraction of the log ratio attributable to hedging
    # (total_ratio - cf_ratio) / (total_ratio - 1) when total_ratio > 1
    if (total_premium > 1.001) {
      hedge_share <- (total_premium - cf_premium) / (total_premium - 1)
    } else {
      hedge_share <- NA
    }

    results <- rbind(results, data.frame(
      delta_g = dg,
      lambda  = lam,
      vA      = res$vA,
      vN      = res$vN,
      ratio   = total_premium,
      cf_ratio = cf_premium,
      hedge_share = hedge_share
    ))
  }
}

# Print LaTeX table
cat("\\begin{table}[t]\n")
cat("\\centering\n")
cat("\\caption{AI valuation premium with differential pre-singularity growth. Each cell reports $v^A/v^N$ at $t=0$, with the hedging share in parentheses (fraction of the premium attributable to the hedging amplifier). Baseline parameters as in Table~\\ref{tab:calibration}.}\n")
cat("\\label{tab:differential}\n")
cat("\\medskip\n")
cat("\\begin{tabular}{@{}cccc@{}}\n")
cat("\\toprule\n")
cat("& \\multicolumn{3}{c}{$\\lambda$} \\\\\n")
cat("\\cmidrule(l){2-4}\n")
cat("$g^A - g^N$ & 0.01 & 0.02 & 0.05 \\\\\n")
cat("\\midrule\n")

for (dg in delta_g_vals) {
  sub <- results[results$delta_g == dg, ]
  label <- sprintf("%.0f pp", dg * 100)
  if (dg == 0) label <- "0 pp"
  cells <- sapply(1:nrow(sub), function(i) {
    r <- sub[i, ]
    if (!is.na(r$hedge_share)) {
      sprintf("%.2f \\;(%.0f\\%%)", r$ratio, r$hedge_share * 100)
    } else {
      sprintf("%.2f", r$ratio)
    }
  })
  cat(sprintf("%s & %s \\\\\n", label, paste(cells, collapse = " & ")))
}

cat("\\bottomrule\n")
cat("\\end{tabular}\n")
cat("\\end{table}\n")
