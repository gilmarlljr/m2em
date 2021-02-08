""" RSS Parsing Module """
import logging
import ssl
import feedparser
from bin.models.Manga import Manga
from bin.Models import *

# Remove verification need of feedparser
from bin.rss.UnionMangaRssHelper import UnionMangaRssHelper

ssl._create_default_https_context = ssl._create_unverified_context


def RssParser(args):
    """ Function that handles the coordination of rss parsing """

    # Get all feeds

    db.connection()
    rssdata = Feeds.select().execute()

    logging.info("Checking for new Feed Data...")

    # loop through rss feeds
    for i in rssdata.iterator():

        # Parse feed and check entries
        get_rss(args, i.url)


def get_rss(args, url):
    logging.info("Getting Feeds for %s", url)
    feed = None
    try:
        rss = ''
        if ".xml" in url:
            rss = str(url)
        elif "unionmangas.top" in url or "unionleitor.top" in url:
            rss = UnionMangaRssHelper(url).decode("utf-8")

        feed = feedparser.parse(rss)
    except Exception as identifier:
        logging.warning("Could not load feed: %s", identifier)
    duplicated = 0
    for entry in feed.entries:
        if duplicated == int(args.duplicates):
            logging.warning("Nao foi encontrado nenhum novo cap")
            break
        current_manga = Manga()
        current_manga.load_from_feed(entry, str(feed['feed']['link']))

        # No need to continue if it is already saved :)
        if current_manga.duplicated.exists():
            duplicated += 1
            continue

        current_manga.print_manga()
        current_manga.save()
