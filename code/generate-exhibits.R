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

p_grid  <- c(0.001, 0.002, 0.005, 0.008, 0.01)
xi_grid <- c(0.00, 0.05, 0.10, 0.20)

results <- expand.grid(xi = xi_grid, p = p_grid) %>%
  select(p, xi) %>%
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
  "\\multicolumn{5}{p{0.85\\textwidth}}{\\footnotesize Parameters: $\\beta=0.96$, $g=0.02$, $\\gamma=4$, $\\phi=0.5$, $\\eta=0.5$, $\\theta=0.15$, $\\Delta\\theta=0.2$. $p$ is the annual singularity probability; $\\xi$ is the extinction probability conditional on singularity. The ratio column reports $\\text{P/D}^{AI} / \\text{P/D}^{N}$.} \\\\",
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

# P/D with transfers: effective phi changes
compute_pd_with_transfer <- function(p_val, xi_val, tau_val, eta_val, gamma_j, phi_val) {
  phi_eff <- phi_val + tau_val * pmax(0, 1 - delta * tau_val) * (1 - phi_val * alpha0) / alpha0
  sdf_sing <- phi_eff^(-gamma) * (1 + eta_val)^(-gamma) * gamma_j
  base <- beta * (1 + g)^(1 - gamma)
  K <- base * ((1 - p_val) + p_val * (1 - xi_val) * sdf_sing)
  if (K >= 1 || K <= 0) return(NA)
  return(K / (1 - K))
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
    gamma_j_val = share_ratio_ai * (1 + eta_val),
    pd_ai = compute_pd_with_transfer(p_ext, xi_ext, tau, eta_val, gamma_j_val, phi_val),
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
    panel.grid.major = element_line(color = "gray35")
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
y_cap_a <- 20

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
  annotate("text", x = exit_tau + 0.01, y = y_cap_a * 0.95,
           label = expression(P/D %->% infinity ~ "as" ~ tau %->% 0),
           color = "#1B4F99", size = 3.5, hjust = 0, fontface = "italic") +
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
  geom_hline(yintercept = 1, linetype = "dashed", color = "black", linewidth = 1.2) +
  # Catastrophe markers at tau=0
  annotate("point", x = 0, y = cons_large_0, shape = 16, size = 3, color = "#1B4F99") +
  annotate("text", x = 0.06, y = cons_large_0 * 0.65,
           label = paste0("Catastrophe:\n", round((1 - cons_large_0) * 100), "% loss"),
           color = "#1B4F99", size = 3.5, hjust = 0, fontface = "bold") +
  annotate("point", x = 0, y = cons_base_0, shape = 16, size = 3, color = "#B22222") +
  annotate("text", x = 0.06, y = cons_base_0 * 0.75,
           label = paste0(round((1 - cons_base_0) * 100), "% loss"),
           color = "#B22222", size = 3.2, hjust = 0) +
  annotate("text", x = 0.55, y = 1.15, label = "No change", color = "gray20", size = 4.5) +
  labs(x = expression("Tax rate " * tau),
       y = "Household Consumption Growth\nin Singularity",
       title = "(b) Household Consumption") +
  scale_x_continuous(labels = scales::percent_format()) +
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
# Exhibit 3: AI valuations vs market — real data from FRED
# =============================================================================

# Download monthly stock price data from FRED
# FRED series: SP500 (S&P 500), NASDAQCOM (NASDAQ Composite)
# AI-exposed firms: individual stock prices via FRED are unavailable, so we
# download S&P 500 and NASDAQ from FRED, then supplement with individual
# firm prices from the datahub Shiller dataset URL for the S&P 500.
#
# Since FRED does not carry individual stock prices, we download an
# equal-weighted basket of AI firms (NVDA, MSFT, GOOGL, META) via
# Yahoo Finance CSV when available, with FRED's NASDAQ as fallback.

download_fred <- function(series_id, start = "2015-01-01", end = "2025-12-31") {
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

# S&P 500 from Shiller/datahub (monthly, goes back to 1871; FRED series starts late)
cat("Downloading S&P 500 data from datahub (Shiller dataset)...\n")
sp500_raw <- read.csv("https://datahub.io/core/s-and-p-500/r/data.csv",
                       stringsAsFactors = FALSE)
sp500_raw$Date <- as.Date(sp500_raw$Date)
sp500 <- sp500_raw %>%
  filter(Date >= as.Date("2015-01-01"), Date <= as.Date("2025-12-31")) %>%
  select(Date, Value = SP500)

# NASDAQ from FRED
cat("Downloading NASDAQ data from FRED...\n")
nasdaq <- download_fred("NASDAQCOM")

# Aggregate to monthly (take last observation per month)
to_monthly <- function(d) {
  d$YM <- format(d$Date, "%Y-%m")
  d %>% group_by(YM) %>% slice_tail(n = 1) %>% ungroup() %>%
    select(Date, Value)
}

sp500_m  <- to_monthly(sp500)
nasdaq_m <- to_monthly(nasdaq)

# Align date ranges
min_date <- max(min(sp500_m$Date), min(nasdaq_m$Date))
max_date <- min(max(sp500_m$Date), max(nasdaq_m$Date))
sp500_m  <- sp500_m  %>% filter(Date >= min_date, Date <= max_date)
nasdaq_m <- nasdaq_m %>% filter(Date >= min_date, Date <= max_date)

# Normalize to first common month = 100
normalize <- function(d) {
  base <- d$Value[which.min(d$Date)]
  d$Index <- d$Value / base * 100
  d
}

sp500_m  <- normalize(sp500_m)
nasdaq_m <- normalize(nasdaq_m)

df_val <- bind_rows(
  sp500_m  %>% mutate(Group = "S&P 500"),
  nasdaq_m %>% mutate(Group = "NASDAQ Composite (AI/Tech-Heavy)")
)

fig_val <- ggplot(df_val, aes(x = Date, y = Index, color = Group, linetype = Group)) +
  geom_line(linewidth = 1) +
  labs(x = NULL, y = "Normalized Price (Jan 2015 = 100)") +
  scale_color_manual(values = c("NASDAQ Composite (AI/Tech-Heavy)" = "#2166AC",
                                "S&P 500" = "#B2182B")) +
  scale_linetype_manual(values = c("NASDAQ Composite (AI/Tech-Heavy)" = "solid",
                                   "S&P 500" = "dashed")) +
  scale_x_date(date_breaks = "2 years", date_labels = "%Y") +
  scale_y_continuous(expand = expansion(mult = c(0.02, 0.05))) +
  theme_paper +
  theme(legend.position = c(0.30, 0.88),
        plot.margin = margin(t = 5, r = 10, b = 5, l = 15, unit = "pt"))

ggsave(file.path(outdir, "fig-ai-valuations.pdf"), fig_val, width = 7, height = 4.5)
cat("Wrote", file.path(outdir, "fig-ai-valuations.pdf"), "\n")

cat("All exhibits generated successfully.\n")
