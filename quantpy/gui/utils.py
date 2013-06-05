import xml.etree.ElementTree as ET
import urllib.request


def fetch_news(tickers, kind='company'):
    """Downloads company news headlines from yahoo

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
