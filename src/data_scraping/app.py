## The scrapy main file
from data_scraping.scrapers import BooksSpider, process

def begin_crawler(start_index : int = 1, end_index : int = 100000):
    process.crawl(BooksSpider, start_index=start_index, end_index=end_index)
    process.start()

if __name__ == "__main__":
    begin_crawler(1, 10000)
