# Example plotting effienct frontier.

import quantpy as qp

# Grap portfolio
P = qp.Portfolio(['GOOG','IBM','INTC','MSFT','AAPL'])

# Plot effiecent frontier
P.efficient_frontier_plot()
