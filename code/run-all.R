#!/usr/bin/env Rscript

# How to run: Rscript code/run-all.R
#   For the CRSP figure, set WRDS_USERNAME and WRDS_PASSWORD environment variables.
#   If WRDS credentials are unavailable, the numerical table is still generated.
# Inputs: WRDS credentials (optional, for CRSP figure).
# Outputs: paper/exhibits/numerical-illustration.tex, paper/exhibits/ai-valuations.pdf

cat("=== Hedging the Singularity: Exhibit Pipeline ===\n\n")

run_script <- function(script) {
  cat(sprintf("--- Running %s ---\n", script))
  ret <- system2("Rscript", script, stdout = "", stderr = "")
  if (ret != 0) stop(sprintf("%s failed with exit code %d", script, ret), call. = FALSE)
}

# ---- Exhibit 2: Numerical Illustration Table ----
run_script("code/numerical-illustration.R")

# ---- Exhibit 1: AI vs Non-AI Valuations Figure ----
tryCatch(
  run_script("code/ai-valuations-figure.R"),
  error = function(e) cat(sprintf("Skipping CRSP figure: %s\n", e$message))
)

cat("\n=== Pipeline complete ===\n")
