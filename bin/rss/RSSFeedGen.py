from feedgen.feed import FeedGenerator


class RSSFeedGen:

    def __init__(self):
        self.feedGen = FeedGenerator()

    def set_header(self, title, link):
        self.feedGen.title(title)
        self.feedGen.description(title)
        self.feedGen.author({'name': 'John Doe', 'email': 'john@example.de'})
        self.feedGen.link(href=link)

    def add_entry(self, title, link, pubdate):
        fe = self.feedGen.add_entry()
        fe.title(title)
        fe.description(title)
        fe.published(pubdate)
        fe.link(href=link)

    def get_rss(self):
        return self.feedGen.rss_str(pretty=True)


if __name__ == '__main__':
    rss = RSSFeedGen()
    rss.set_header('teste', 'teste t', 'link')
    rss.add_entry('entry', 'entry t', 'link')
    print(rss.get_rss())
