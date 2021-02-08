#!/usr/bin/env python
""" Mangafox Parsing Module """
import logging
import re
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup

'''

        MangaFox Parser


'''

'''
get Manga Title
Returns: title
'''


def getTitle(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    var = soup.find("title")
    return str(var.next).split(" - ")[0]


'''
get Manga Chapter name
Returns: Chapter name
'''


def getChapterName(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    var = soup.find("title")
    return str(var.next).split(" - ")[1]


'''
get Manga Pages
Returns: integer pages
'''


def getPages(page):
    soup = BeautifulSoup(page.content, 'html.parser')

    # Get Manga Titel
    search = re.search('var total_pages=(.*?);', str(soup))
    pages = soup.select("select[id=paginas]>option")
    return pages.__len__()


'''
get Manga chapter
Returns: integer chapter
'''


def getChapter(page):
    soup = BeautifulSoup(page.content, 'html.parser')
    var = soup.find("title")
    cap = re.sub(r'\D', '', str(var.next))
    return int(cap)



def getPagesUrl(pageurl):
    page = requests.get(pageurl)
    soup = BeautifulSoup(page.content, 'html.parser')
    img_tags = soup.find_all('img')
    page_urls = [img['src'] for img in img_tags]
    logging.debug("All pages:")
    logging.debug(page_urls)
    return page_urls


def getImageUrl(pageurl):
    return pageurl
