import feedparser
from pprint import pprint
Infobae = feedparser.parse("https://www.infobae.com/feeds/rss/")
Clarin = feedparser.parse("https://www.clarin.com/rss/politica/")
titulos_clarin = Clarin.entries
titulos_infobae = Infobae.entries

#[(tI, tC) for tC in titulos_clarin if titulo.title in [tI for tI in titulos_infobae]]
