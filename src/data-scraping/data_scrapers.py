import scrapy
from scrapy.crawler import CrawlerProcess
from yaml_resolver import XPATH_DATA

class BooksSpider(scrapy.Spider):
    name = "books-spider"

    custom_settings = {
        "DOWNLOAD_DELAY" : 2,
        "RANDOMIZE_DOWNLOAD_DELAY" : True,
        "CONCURRENT_REQUESTS_PER_DOMAIN" : 1
    }

    # Initialising the variable for page data structure and data regex
    def __init__(self, start_index=0, end_index=10):
        super(BooksSpider, self).__init__()
        self.start = start_index
        self.end = end_index
        self.XPATH_dict = XPATH_DATA

    # Making requests to pages based on index , masking UA as web browser
    def start_requests(self):
        urls = (f"https://www.goodreads.com/book/show/{index}" for index in range(self.start,self.end))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    })
    
    # Parsing page data based on yaml schema
    def parse(self, response):
        final_data = dict()
        if not self.exclude_page(response):
            final_data["index"] = response.url.split("/")[-1]


            for data_variable , data_dict in self.XPATH_dict["data_pages"].items():
                regex_ = data_dict["regex"]
                if not data_dict["data_source"]: # Skipping non data entries (Custom enabling)
                    continue 
                if data_dict["regex"] == "": # Skipping non regex entries (For validating)
                    continue
                final_data[data_variable] = response.xpath(data_dict["xpath"]).re(regex_)
            yield final_data


    def exclude_page(self, response):
        for exclusion_xpath in XPATH_DATA["exclude"].values():
            if response.xpath(exclusion_xpath).get() != None:
                return True
        else:
            return False


process = CrawlerProcess(
    settings={
        "FEEDS": {
            "./data/data_preview_1.jsonl": {"format": "jsonl"},
        },
    }
)

