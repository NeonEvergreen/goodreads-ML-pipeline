## The scrapy main file
from data_scrapers import BooksSpider, process


if __name__ == "__main__":
    process.crawl(BooksSpider, start_index=1, end_index=100)
    process.start()