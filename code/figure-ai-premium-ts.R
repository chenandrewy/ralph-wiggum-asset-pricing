# Generate Figure 2: AI valuation premium and AI capability milestones
# Input:  data/ai-vs-market-pd.csv, data/ai-vs-market-pe.csv
# Output: paper/figure-ai-premium-ts.pdf
# Run:    Rscript code/figure-ai-premium-ts.R

pd <- read.csv("data/ai-vs-market-pd.csv", comment.char = "#")
pe <- read.csv("data/ai-vs-market-pe.csv", comment.char = "#")

pd$ratio <- pd$ai_pd / pd$market_pd
pe$ratio <- pe$ai_pe / pe$market_pe

pdf("paper/figure-ai-premium-ts.pdf", width = 6.5, height = 3.5)
par(mar = c(3.5, 4, 0.5, 0.5), mgp = c(2.2, 0.6, 0))

plot(pd$year, pd$ratio,
     type = "b", pch = 16, lwd = 2,
     xlab = "", ylab = "AI / market ratio",
     ylim = c(1.0, 3.0), xaxt = "n",
     panel.first = grid(col = "gray90"))
axis(1, at = 2015:2024)
lines(pe$year, pe$ratio, type = "b", pch = 17, lwd = 2, lty = 3)

# AI capability milestones
abline(v = 2020, lty = 2, col = "gray50")
abline(v = 2023, lty = 2, col = "gray50")
text(2020, 2.90, "GPT-3", cex = 0.7, pos = 2, col = "gray40")
text(2023, 2.90, "ChatGPT /\nGPT-4", cex = 0.7, pos = 4, col = "gray40")

# Reference line at 1
abline(h = 1, lty = 3, col = "gray70")

legend("topleft",
       legend = c("Price / total payout", "Price / earnings"),
       lty = c(1, 3), pch = c(16, 17), lwd = 2, bty = "n", cex = 0.9)

dev.off()
cat("Saved paper/figure-ai-premium-ts.pdf\n")
