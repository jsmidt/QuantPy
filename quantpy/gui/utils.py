import xml.etree.ElementTree as ET
import urllib.request


def fetch_company_news(symbols):
    """Downloads company news headlines from yahoo

    symbols is a comma separated list of symbols: yhoo,msft,tivo
    or just one symbol

    """
    if not symbols:
        return None

    feed = urllib.request.urlopen(
        'http://finance.yahoo.com/rss/headline?s=%s' % symbols
    )

    tree = ET.parse(feed)
    root = tree.getroot()
    print(root.attrib)
    news = []
    for item in root.iter('item'):
        news.append({
            'description': item.find('description').text,
            'link': item.find('link').text,
            'pub_date': item.find('pubDate').text,
            'title': item.find('title').text,
        })

    return news
