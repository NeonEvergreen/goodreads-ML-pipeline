from data_scraping import app

def main():
    app.begin_crawler(1, 10000)

if __name__ == "__main__":
    main()
