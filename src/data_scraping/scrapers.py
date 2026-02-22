# other packages
from typing import Self
# External dependencies
from data_scraping import data_ingestion
from data_scraping.yaml_resolver import XPATH_DATA
from data_scraping.settings import CRAWLER_DELAY
from settings import DATA_DIR
# Scrapy stuff
import scrapy
import scrapy.loader
from scrapy.crawler import CrawlerProcess

class BooksSpider(scrapy.Spider):
    name = "books-spider"

    custom_settings = {
        "DOWNLOAD_DELAY" : CRAWLER_DELAY, ## Crawler delay configuration
        "RANDOMIZE_DOWNLOAD_DELAY" : True,
        "CONCURRENT_REQUESTS_PER_DOMAIN" : 1    # Scraping ethics
        # ,"ITEM_PIPELINES" : {"pipeline.JsonItemWriter": 100}
    }

    # Initialising the variable for page data structure and data regex
    def __init__(self, start_index=0, end_index=10):
        super(BooksSpider, self).__init__()
        self.start_index = int(start_index)
        self.end_index = int(end_index)
        self.XPATH_dict = XPATH_DATA

    # Making requests to pages based on index , masking UA as web browser
    def start_requests(self):
        urls = (f"https://www.goodreads.com/book/show/{index}" for index in range(self.start_index,self.end_index))
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers={
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
    })
    
    # Parsing page data based on yaml schema
    def parse(self, response):

        if response.status != 200:
            self.logger.warning(f"Non 200 response :\n {response.status} :: {response.url}")
            return
        
        if self.exclude_page(response):
            return #Exclude page check and skip
        
        try:    
            index_num = response.url.split("/")[-1]
        
            loader = scrapy.loader.ItemLoader(item=data_ingestion.generate_data_page_schema()())
            loader.add_value("index", index_num)

            for data_variable , data_dict in self.XPATH_dict["data_pages"].items():
                regex_ = data_dict["regex"]
                if not data_dict["data_source"]: # Skipping non data entries (Custom enabling)
                    continue
                if data_dict["regex"] == "": # Skipping non regex entries (For validating)
                    continue
                ## Data Extraction from DOM
                element_data = response.xpath(data_dict["xpath"]).re(regex_)
                data_loader = data_ingestion.data_formatter_loader(
                    data_labels=data_dict["data_labels"],
                    data_list=element_data, 
                    data_types=data_dict["data_type"],
                    loader=loader)
                
                 
            ## Yielding load
            yield data_loader.load_item() # Requires a itemadapter class expansion


        except Exception as e:
            self.logger.error(f"Error :: \n{response.url}\n{e}")
            return


    def exclude_page(self : Self, response : dict)-> bool: # List of exclusion identifiers in pages to skip them
        for exclusion_xpath in XPATH_DATA["exclude"].values():
            if response.xpath(exclusion_xpath).get() != None:
                return True
        else:
            return False


process = CrawlerProcess(
    settings={
        "FEEDS": {
            DATA_DIR / "data_preview_1.jsonl": {"format": "jsonl"},
        },
    }
)

