# How to run: Rscript code/figure-mechanism.R
# Inputs: None (parameters defined inline)
# Outputs: paper/figure-mechanism.pdf

# --- Parameters (baseline calibration) ---
beta  <- 0.96
gamma <- 3
g     <- 0.02
phi   <- 0.30
phi_L <- 0.20
s     <- 0.05
ell   <- 0.65
lambda <- 0.02
delta_H <- 0

a <- beta * (1 + g)^(1 - gamma)  # effective discount factor

# Friction-resolution parameters
# pi(theta) = Y_O / (d + Y_O), Y_O = theta^2 (super-linear)
d_fric <- 2  # aggregated friction parameter

# --- Grid over theta ---
theta_grid <- seq(0.01, 8, by = 0.01)

# --- Compute components ---
J_fun <- function(theta) {
  s * (1 + theta) + (1 - s - ell) * (1 - phi) + ell * (1 - phi_L)
}

pi_fun <- function(theta) {
  Y_O <- theta^2
  Y_O / (d_fric + Y_O)
}

K <- lambda * (1 - delta_H) * a / ((1 - a) * (1 - (1 - lambda) * a))

cash_flow <- function(theta) {
  K * (theta + phi)
}

total_premium <- function(theta) {
  J <- J_fun(theta)
  pi_val <- pi_fun(theta)
  K * (theta + phi) * ((1 - pi_val) * J^(-gamma) + pi_val)
}

hedge_component <- function(theta) {
  J <- J_fun(theta)
  pi_val <- pi_fun(theta)
  K * (theta + phi) * (1 - pi_val) * (J^(-gamma) - 1)
}

cf_vals    <- sapply(theta_grid, cash_flow)
total_vals <- sapply(theta_grid, total_premium)
hedge_vals <- sapply(theta_grid, hedge_component)

# --- Plot ---
pdf("paper/figure-mechanism.pdf", width = 6, height = 4.2)
par(mar = c(4.2, 4.5, 1.5, 1), family = "serif")

y_max <- max(total_vals[theta_grid <= 6]) * 1.05
y_min <- min(hedge_vals[theta_grid <= 6]) * 1.1

plot(NULL, xlim = c(0, 6), ylim = c(y_min, y_max),
     xlab = expression(theta ~ "(AI dividend jump)"),
     ylab = expression(v^A - v^N ~ "(premium)"),
     las = 1, cex.lab = 1.1, cex.axis = 0.9)

# Shading for hedging component
polygon(c(theta_grid[theta_grid <= 6], rev(theta_grid[theta_grid <= 6])),
        c(cf_vals[theta_grid <= 6], rev(total_vals[theta_grid <= 6])),
        col = rgb(0.2, 0.4, 0.8, 0.15), border = NA)

lines(theta_grid, total_vals, lwd = 2.2, col = "black")
lines(theta_grid, cf_vals, lwd = 2.2, col = "gray40", lty = 2)
lines(theta_grid, hedge_vals, lwd = 2.2, col = rgb(0.2, 0.4, 0.8))

abline(h = 0, col = "gray70", lty = 3)

# Mark baseline theta
abline(v = 0.50, col = "gray60", lty = 3, lwd = 0.8)
text(0.50, y_max * 0.95, expression(theta == 0.50), pos = 4, cex = 0.75, col = "gray40")

legend("topright",
       legend = c("Total premium", "Cash-flow premium", "Hedging component"),
       col = c("black", "gray40", rgb(0.2, 0.4, 0.8)),
       lty = c(1, 2, 1), lwd = 2, cex = 0.85, bg = "white")

dev.off()
