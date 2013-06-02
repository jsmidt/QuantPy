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

    Paramters:

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
