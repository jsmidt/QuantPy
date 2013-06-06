import xml.etree.ElementTree as ET
import urllib.request

import numpy as np
import pandas as pd

from quantpy.gui import settings


def fetch_news(tickers, kind='company'):
    """Download company news headlines from yahoo

    'tickers' is a comma separated list of tickers: yhoo,msft,tivo
    or just one ticker symbol

    'kind' can either be 'company' or 'industry'. If it's 'industry' industry
    (that the company belongs to) news will be fetched. A ValueError is raised
    if kind if neither 'company' nor 'industry'.
    """
    if not tickers:
        return None

    if not kind in ('company', 'industry'):
        raise ValueError("'kind' must be one of 'company' or 'industry'.")

    if kind == 'company':
        url = 'http://finance.yahoo.com/rss/headline?s=%s' % tickers
    else:
        url = 'http://finance.yahoo.com/rss/industry?s=%s' % tickers

    feed = urllib.request.urlopen(url)

    tree = ET.parse(feed)
    root = tree.getroot()

    news = []
    for item in root.iter('item'):
        try:
            news.append({
                'description': item.find('description').text,
                'link': item.find('link').text,
                'pub_date': item.find('pubDate').text,
                'title': item.find('title').text,
            })
        except AttributeError:
            pass

    return news


def get_market_updates(symbols, special_tags):
    """
    Get current yahoo quote.

    'special_tags' is a list of tags. More info about tags can be found at
    http://www.gummy-stuff.org/Yahoo-data.htm

    Returns a DataFrame
    """
    if isinstance(symbols, str):
        sym_list = symbols
    elif not isinstance(symbols, pd.Series):
        symbols = pd.Series(symbols)
        sym_list = str.join('+', symbols)
    else:
        sym_list = str.join('+', symbols)

    # Symbol must be in the special_tags for now
    if not 's' in special_tags:
        special_tags.insert(0, 's')
    request = ''.join(special_tags)  # code request string
    special_tag_names = [settings.YAHOO_SYMBOL_TAGS[x] for x in special_tags]
    header = special_tag_names

    data = dict(list(zip(
        list(special_tag_names), [[] for i in range(len(special_tags))]
    )))

    urlStr = 'http://finance.yahoo.com/d/quotes.csv?s=%s&f=%s' % (
        sym_list, request)

    try:
        lines = urllib.request.urlopen(urlStr).readlines()
    except Exception as e:
        s = "Failed to download:\n{0}".format(e)
        print(s)
        return None

    for line in lines:
        fields = line.decode('utf-8').strip().split(',')
        for i, field in enumerate(fields):
            if field[-2:] == '%"':
                data[header[i]].append(float(field.strip('"%')))
            elif field[0] == '"':
                data[header[i]].append(field.strip('"'))
            else:
                try:
                    data[header[i]].append(float(field))
                except ValueError:
                    data[header[i]].append(np.nan)

    idx = data.pop('Symbol')

    return pd.DataFrame(data, index=idx)


def get_dashboard_index_updates():
    """Fetch updates for assets in the settings.DASHBOARD_INDEXES
    Return a pandas data frame.
    """
    symbols = [x for x in settings.DASHBOARD_INDEXES.keys()]
    special_tags = ['s', 'c6', 'd1', 'l1', 'p2']  # settings.YAHOO_SYMBOL_TAGS
    return get_market_updates(symbols, special_tags)
