# This concept was inspired by QSTK:
# http://wiki.quantsoftware.org/index.php?title=QuantSoftware_ToolKit.
# However, no source code from that toolkit was used or consulted directly for
# this code.  (The concept only)
from pylab import errorbar, xlabel, ylabel, show, legend
from numpy import array, arange


def event_profiler(asset, truth, periods=5):
    cut = []
    for i in range(periods, len(asset) - periods):
        if truth[i] == 1 and asset[i] > 0:
            cut.append(asset[i - periods:i + periods] / asset[i])
    return array(cut)


def plot_event_profile(events, name=''):
    mn = events.mean(axis=0) - 1.0
    st = events.std(axis=0)
    errorbar(arange(len(mn)), mn, st, label=name)
    xlabel('Periods', fontsize=16)
    ylabel('Price Change %', fontsize=16)
    if len(name) > 1:
        legend(loc='best', shadow=True, fancybox=True)
    show()
