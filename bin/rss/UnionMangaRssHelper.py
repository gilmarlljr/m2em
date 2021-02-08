from datetime import datetime

import pytz as pytz

from bin.rss.RSSFeedGen import RSSFeedGen
import requests
from bs4 import BeautifulSoup


def UnionMangaRssHelper(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    list_cap_tags = soup.select('div > div > a[href*="/leitor"]')
    list_cap_date_tags = soup.select('div > div > span[style*="font-size: 10px; color: #999;"]')
    name = soup.find('h2')
    rss = RSSFeedGen()
    rss.set_header(str(name.next), url)
    timezone = pytz.timezone("UTC")

    for i in range(list_cap_tags.__len__()-1, -1, -1):
        cap = list_cap_tags[i]
        cap_date = list_cap_date_tags[i]
        with_timezone = timezone.localize(datetime.strptime(str(cap_date.next), '(%d/%m/%Y)'))
        rss.add_entry(str(cap.next), cap['href'], with_timezone)
    return rss.get_rss()


if __name__ == '__main__':
    UnionMangaRssHelper("https://unionmangas.top/perfil-manga/shingeki-no-kyojin")
