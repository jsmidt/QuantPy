import portfolio
from event_profiler import *
from numpy import *


# Create your own truth function describing your even.
# In this case the event is: whenever the price chanegs $1.
def truth_function(asset):
    truth = zeros(len(asset))
    for i in range(1,len(asset)):
       if  asset[i] - asset[i-1] > 1.0:
           truth[i] = 1
    return truth


# Grab a profile
P = portfolio.Portfolio(['GOOG','IBM','INTC'])

# Define your asset you want to test.
asset = P.asset['IBM']['Adj Close']

# Generate your truth function.
truth = truth_function(asset)

# Get profiles for these events
profiles = event_profiler(asset,truth)

# Plot them
plot_event_profile(profiles,name='When price increases $1.')
