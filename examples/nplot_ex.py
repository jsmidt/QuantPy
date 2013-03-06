# Example plotting returns.
from pylab import *
import portfolio

# Get symbols.
syms = ['IBM','GOOG','MSFT','AAPL','INTC']
cols = ['b','r','g','k','m','y']

# Get portfolio
P = portfolio.Portfolio(syms)

# Make plots of normalized returns.
for sym,col in zip(syms,cols):
    P.nplot(sym,col)
show()
