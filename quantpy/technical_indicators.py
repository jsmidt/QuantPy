import numpy as np
import pandas as pd


def sma(data, window):
    """Simple Moving Average: The average price of a security over a
    specific number of periods.

    'data' is a pandas Series or DataFrame of prices. A ValueError is raised
    if 'data' is of different data type.

    'window' is the number of observations.
    It must be a positive integer less than or equal to the length of the data.
    Otherwise a ValueError will be raised.
    """

    # todo: maybe add 'long' too?
    if not isinstance(window, int) or not 0 < window <= len(data):
        raise ValueError("'window' must be an integer " +
                         "between 1 and %d." % len(data))

    if not isinstance(data, (pd.Series, pd.DataFrame)):
        raise ValueError("'data' must be a pandas Series or DataFrame.")

    return pd.rolling_mean(data, window)


def smstd(data, window):
    """Simple Moving Standard Deviation: The standard deviation price of a
    security over a specific number of periods.

    'data' is a pandas Series or DataFrame of prices. A ValueError is raised
    if 'data' is of different data type.

    'window' is the number of observations.
    It must be a positive integer less than or equal to the length of the data.
    Otherwise a ValueError will be raised.
    """

    # todo: maybe add 'long' too?
    if not isinstance(window, int) or not 0 < window <= len(data):
        raise ValueError("'window' must be an integer " +
                         "between 1 and %d." % len(data))

    if not isinstance(data, (pd.Series, pd.DataFrame)):
        raise ValueError("'data' must be a pandas Series or DataFrame.")

    return pd.rolling_std(data, window)


def ema(data, window):
    """Exponential Moving Average: The exponentially weighted average price of
    a security over a specific number of periods.

    'data' is a pandas Series or DataFrame of prices. A ValueError is raised
    if 'data' is of different data type.

    'window' is the number of observations.
    It must be a positive integer less than or equal to the length of the data.
    Otherwise a ValueError will be raised.
    """

    # todo: maybe add 'long' too?
    if not isinstance(window, int) or not 0 < window <= len(data):
        raise ValueError("'window' must be an integer " +
                         "between 1 and %d." % len(data))

    if not isinstance(data, (pd.Series, pd.DataFrame)):
        raise ValueError("'data' must be a pandas Series or DataFrame.")

    return pd.ewma(data, span=window)


def emstd(data, window):
    """Exponential Moving Standard Deviation: The exponentially weighted
    standard deviation of the price of a security over a specific number of
    periods.

    'data' is a pandas Series or DataFrame of prices. A ValueError is raised
    if 'data' is of different data type.

    'window' is the number of observations.
    It must be a positive integer less than or equal to the length of the data.
    Otherwise a ValueError will be raised.
    """

    # todo: maybe add 'long' too?
    if not isinstance(window, int) or not 0 < window <= len(data):
        raise ValueError("'window' must be an integer " +
                         "between 1 and %d." % len(data))

    if not isinstance(data, (pd.Series, pd.DataFrame)):
        raise ValueError("'data' must be a pandas Series or DataFrame.")

    return pd.ewmstd(data, span = window)


def macd(data, ema_fast=12, ema_slow=26, ema_macd=9):
    """Moving Average Convergence/Divergence.

    Parameters:

        'data' is a pandas Series or DataFrame of prices. A ValueError is
        raised if 'data' is of different data type.

        'ema_fast' The window period of the "fast" EMA. (Default = 12)

        'ema_slow' The window period of the "slow" EMA. (Default = 26)

    Returns:

        MACD: The difference between the ema_fast and ema_slow day EMAs of a
        security.

        MACD Signal: The ema_macd day EMA of the MACD.

        MACD Histogram: Difference between the MACD and MACD Signal.
    """

    # todo: maybe add 'long' too?
    if not isinstance(ema_fast, int) or not 0 < ema_fast <= len(data):
        raise ValueError("'ema_fast' must be an integer " +
                         "between 1 and %d." % len(data))

    if not isinstance(ema_slow, int) or not 0 < ema_slow <= len(data):
        raise ValueError("'ema_slow' must be an integer " +
                         "between 1 and %d." % len(data))

    if not isinstance(data, (pd.Series, pd.DataFrame)):
        raise ValueError("'data' must be a pandas Series or DataFrame.")

    if not isinstance(ema_macd, int) or not 0 < ema_macd <= len(data):
        raise ValueError("'ema_macd' must be an integer " +
                         "between 1 and %d." % len(data))

    macd = pd.ewma(data, span = ema_fast) - pd.ewma(data, span = ema_slow)
    macds = pd.ewma(macd, span = ema_macd)

    return macd, macds, macd - macds

def full_stochastic(data, lookback = 14, d_sma = 3, full_sma = 3):
    """Full Stochastic Oscillator: The full stochastic oscillator for
       (lookback,d_sma,full_sma) is defined by:

       %K = (Current Close - Lowest Low)/(Highest High - Lowest Low) * 100
       %D = d_sma-day SMA of %K
       full %K = %D
       full %D = full_sma-day SMA of full %K

    Parameters:

        'data' is a pandas Series or DataFrame of prices. Must contain
               'High', 'Low' and 'Close' information.

        'lookback' Lookback period for calculating highest and Lowst low

        'd_sma'    The SMA used for calculating %D

        'full_sma' The SMA used for calculating full %D

    Returns:

        full %K: (Or standard %D) as defined above

        full %D: as defined above

        %K: Standard %K as defined above
    """

    l_low = pd.rolling_min(data['Low'], lookback) 
    h_high = pd.rolling_max(data['High'], lookback) 

    K = (data['Close'] - l_low)/(h_high - l_low) * 100.0
    full_K = pd.rolling_mean(K,d_sma)
    full_D = pd.rolling_mean(full_K,full_sma)

    return full_K, full_D, K 

