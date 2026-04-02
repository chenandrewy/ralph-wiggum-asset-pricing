#!/usr/bin/env Rscript

# How to run: WRDS_USERNAME=<user> WRDS_PASSWORD=<pw> Rscript code/ai-valuations-figure.R
#   (or sourced from run-all.R)
# Inputs: WRDS credentials via environment variables.
# Outputs: paper/exhibits/ai-valuations.pdf

suppressPackageStartupMessages({
  library(DBI)
  library(RPostgres)
})

outfile <- "paper/exhibits/ai-valuations.pdf"

# --- WRDS connection ---
username <- Sys.getenv("WRDS_USERNAME", unset = Sys.getenv("PGUSER", unset = ""))
password <- Sys.getenv("WRDS_PASSWORD", unset = Sys.getenv("PGPASSWORD", unset = ""))
host <- Sys.getenv("WRDS_HOST", unset = "wrds-pgdata.wharton.upenn.edu")
port <- as.integer(Sys.getenv("WRDS_PORT", unset = "9737"))
dbname <- Sys.getenv("WRDS_DBNAME", unset = "wrds")
sslmode <- Sys.getenv("WRDS_SSLMODE", unset = "require")

if (username == "") {
  stop("WRDS credentials not set. Set WRDS_USERNAME to generate the CRSP figure.",
       call. = FALSE)
}

connect_args <- list(
  drv = Postgres(),
  host = host,
  port = port,
  dbname = dbname,
  user = username,
  sslmode = sslmode
)
if (password != "") {
  connect_args$password <- password
}

con <- do.call(dbConnect, connect_args)
on.exit(dbDisconnect(con), add = TRUE)

cat("  Connected to WRDS.\n")

# --- Query: Monthly prices and dividends for AI vs broad market ---
# AI tickers: NVDA, MSFT, GOOG/GOOGL, META, AMZN
# We use CRSP monthly stock file and distributions for trailing 12-month dividends.
# Compute price-dividend ratios at the portfolio level.

query <- "
WITH ai_permnos AS (
  SELECT DISTINCT a.permno
  FROM crsp.stocknames a
  WHERE a.ticker IN ('NVDA', 'MSFT', 'GOOGL', 'META', 'AMZN')
    AND a.namedt <= '2025-12-31'
    AND a.nameenddt >= '2018-01-01'
),
monthly AS (
  SELECT m.permno, m.date,
         ABS(m.prc) AS prc, m.shrout,
         ABS(m.prc) * m.shrout AS mcap
  FROM crsp.msf m
  WHERE m.date BETWEEN '2018-01-01' AND '2025-12-31'
    AND m.prc IS NOT NULL
    AND m.shrout IS NOT NULL
    AND m.shrout > 0
),
divs AS (
  SELECT d.permno,
         DATE_TRUNC('month', d.exdt)::date AS month,
         SUM(d.divamt) AS div_total
  FROM crsp.msedist d
  WHERE d.exdt BETWEEN '2017-01-01' AND '2025-12-31'
    AND d.divamt > 0
  GROUP BY d.permno, DATE_TRUNC('month', d.exdt)::date
)
SELECT m.date,
       CASE WHEN ai.permno IS NOT NULL THEN 'AI' ELSE 'Non-AI' END AS group_label,
       SUM(m.mcap) AS total_mcap,
       SUM(m.mcap / NULLIF(m.prc, 0) * COALESCE(d.div_total, 0)) AS total_div_shares
FROM monthly m
LEFT JOIN ai_permnos ai ON m.permno = ai.permno
LEFT JOIN divs d ON m.permno = d.permno
  AND DATE_TRUNC('month', m.date)::date = d.month
GROUP BY m.date, CASE WHEN ai.permno IS NOT NULL THEN 'AI' ELSE 'Non-AI' END
ORDER BY m.date, group_label
"

cat("  Running CRSP query...\n")
df <- dbGetQuery(con, query)
cat(sprintf("  Retrieved %d rows.\n", nrow(df)))

# --- Compute trailing 12-month P/D ratios by group ---
df$date <- as.Date(df$date)

# For each group-month, compute trailing 12-month dividends
groups <- split(df, df$group_label)
result_list <- list()

for (grp_name in names(groups)) {
  grp <- groups[[grp_name]]
  grp <- grp[order(grp$date), ]

  # Rolling 12-month dividend sum
  n <- nrow(grp)
  grp$trail_div <- NA_real_
  for (i in 1:n) {
    window_start <- grp$date[i] - 365
    window <- grp$date >= window_start & grp$date <= grp$date[i]
    grp$trail_div[i] <- sum(grp$total_div_shares[window], na.rm = TRUE)
  }
  grp$pd_ratio <- ifelse(grp$trail_div > 0, grp$total_mcap / grp$trail_div, NA)
  result_list[[grp_name]] <- grp
}

ai_data <- result_list[["AI"]]
nonai_data <- result_list[["Non-AI"]]

# Filter to 2019+ for cleaner trailing window
ai_data <- ai_data[ai_data$date >= as.Date("2019-01-01"), ]
nonai_data <- nonai_data[nonai_data$date >= as.Date("2019-01-01"), ]

# --- Plot ---
pdf(outfile, width = 7, height = 4.5)
par(mar = c(4, 4.5, 2, 1))

ylim <- range(c(ai_data$pd_ratio, nonai_data$pd_ratio), na.rm = TRUE)
ylim[2] <- min(ylim[2], 500)  # Cap for readability

plot(ai_data$date, ai_data$pd_ratio, type = "l", lwd = 2, col = "steelblue",
     xlab = "", ylab = "Price / Trailing 12-Month Dividends",
     ylim = ylim, main = "AI vs. Non-AI Stock Valuations (CRSP)",
     las = 1, cex.main = 1.1)
lines(nonai_data$date, nonai_data$pd_ratio, lwd = 2, col = "firebrick")
legend("topleft", legend = c("AI Stocks", "Non-AI Stocks"),
       col = c("steelblue", "firebrick"), lwd = 2, bty = "n", cex = 0.9)

dev.off()
cat(sprintf("  Figure written to %s\n", outfile))
