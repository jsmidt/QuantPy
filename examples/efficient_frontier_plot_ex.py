# Example plotting effienct frontier.

import portfolio

# Grap portfolio
P = portfolio.Portfolio(['GOOG','IBM','INTC','MSFT','AAPL'])

# Plot effiecent frontier
P.efficient_frontier_plot()
