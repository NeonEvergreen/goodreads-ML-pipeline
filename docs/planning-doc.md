# Plans

## SCRAPING
### Data source (confirmed)
1) Decision to scrape two data sources
    * Book information
    * Author information
2) NOTE : Need to incorporate scrapy-playwright to collect "language" and "ASIN" information
https://github.com/scrapy-plugins/scrapy-playwright

### Schema for extraction (confirmed)
~~1) All data schema and extraction specifications to be stored within element-xpath-queue.yaml file.~~
~~2) Data variable name and type will also be qualified here.~~


NOTE : Create scrapy.Item and scrapy.Field() to FORMAT, STRUCTURE and GENERIC CLEAN data

### Schema for formatting (in planning stage) (ETL)
~~1) Another schema required for Formatting data to correct format. Need to plan on this. (planning)~~
~~2) Possible module with respective lambda functions tied to variable names (planning)~~
~~3) functions for parsing, cleaning. (planning)~~


### TESTS For above
1) Robust tests need to be added to confirm this schema is maintained. (data type, data size, validation logic pass, various case handlings, random tests, Summary logging)

### Fast api service wrapping
1) Wrap Extraction process as a fastapi service

### Efficient scraping (in planning stage)
1) The scraping will be planned asynchronously for different index groups.
2) Need a state maintenance for the asynchronous operation. probably a json or yaml.
3) __PRIORITY__ : Need rate limiters to avoid ip blocking. **Need a way to determine ratio of scraping to rest.**
4) __PRIORITY__ : Need a way to skip scraping on pages where other or other information is shown.
5) __PRIORITY__ : Logging of Errors required.
6) __PRIORITY__ : Need to scramble information like "agent/browser", "device" etc. to avoid blockage.
7) Need to give an estimator and scraping per page metric monitor.

__Milestome__ : 1 Million efficient Scrapes. With minimal errors and no unidentified errors.
__Goal__ : Possible of 3 billion + books with equivalent or less than that author pages.


## DATA STORAGE (Not Started)
### Data Schema
1) PostGres DB.
2) Snowflake Schema. (in Planning stage)
3) Thread safety confirmation. (in Planning stage)
