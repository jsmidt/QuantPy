from pylab import *
import portfolio

# Get portf
P = portfolio.Portfolio(['IBM','GOOG','MSFT','AAPL','INTC'])


bb = P.ret_for_w(ones(5))
cumsum(bb).plot(color='r',label='Buy and Hold Equally.')
mm = cumsum(bb)[-1]


w = P.min_var_w_ret(mm)
aa = P.ret_for_w(w)
cumsum(aa).plot(label='Same return but min variance.')
legend(loc='best',shadow=True, fancybox=True)
show()


