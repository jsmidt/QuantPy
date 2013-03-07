# Example plotting returns.
from pylab import *
import quantpy as qp

# Get symbols.
syms = ['IBM','GOOG','MSFT','AAPL','INTC']
cols = ['b','r','g','k','m','y']

# Get portfolio
P = qp.Portfolio(syms)

# Make plots of normalized returns.
for sym,col in zip(syms,cols):
    P.nplot(sym,col)
show()
