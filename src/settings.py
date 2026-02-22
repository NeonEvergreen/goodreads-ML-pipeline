from pathlib import Path

CURRENT_DIR = Path(__file__).parent.resolve()
SCRAPER_DIR = CURRENT_DIR / "data_scraping"
DATA_DIR = CURRENT_DIR.parent / "data" / "scraped_data"