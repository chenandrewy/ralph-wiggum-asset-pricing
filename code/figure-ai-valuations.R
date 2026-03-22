# Generate Figure 1: AI stock valuations vs market portfolio
# Input:  data/ai-vs-market-pd.csv
# Output: paper/figure-ai-valuations.pdf
# Run:    Rscript code/figure-ai-valuations.R

df <- read.csv("data/ai-vs-market-pd.csv", comment.char = "#")

pdf("paper/figure-ai-valuations.pdf", width = 6.5, height = 3.5)
par(mar = c(3.5, 4, 0.5, 0.5), mgp = c(2.2, 0.6, 0))

plot(df$year, df$ai_pd,
     type = "b", pch = 16, lwd = 2,
     xlab = "", ylab = "Price / total payout",
     ylim = c(10, 90), xaxt = "n",
     panel.first = grid(col = "gray90"))
axis(1, at = 2015:2024)
lines(df$year, df$market_pd, type = "b", pch = 17, lwd = 2, lty = 3)
legend("topleft", legend = c("AI stocks", "Market portfolio"),
       lty = c(1, 3), pch = c(16, 17), lwd = 2, bty = "n", cex = 0.9)

dev.off()
cat("Saved paper/figure-ai-valuations.pdf\n")
