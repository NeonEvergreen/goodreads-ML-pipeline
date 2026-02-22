import yaml
from pathlib import Path
import os
from settings import SCRAPER_DIR, DATA_DIR
import json

def yaml_resolver():
    default_path = SCRAPER_DIR / "element-xpaths" / "element-xpath-queue.yaml"
    if default_path.exists():
        return default_path
    else:
        raise FileNotFoundError(
            "Sorry! The original xpath data is redacted for ethical purposes!"
        )

# def fetch_last_index(jsonl_path : Path) -> int:
#     try:
#         with open(jsonl_path, mode="rb") as f:
#             try:  ## In case our file only has 1 line and no newlines
#                 f.seek(-2, os.SEEK_END) ## Go two bytes from the file end
#                 while f.read(1) != b'\n': ## check if a newline binary character "\n" is found
#                     f.seek(-2, os.SEEK_CUR)
#             except OSError:
#                 return 0
#             last_line = f.readline().decode() ## Last line fetched and parsed
#             last_index = json.loads(last_line)["index"][0] ### getting last index
#             return int(last_index)

#     except FileNotFoundError:
#         raise FileNotFoundError("The Jsonl file mentioned is missing!")
#     except json.JSONDecodeError:
#         raise TypeError("The Last line of jsonl is not in JSON format!")

with open(yaml_resolver()) as elements_xpath:
    XPATH_DATA = yaml.safe_load(elements_xpath)

print(XPATH_DATA)


if __name__ == "__main__":
    pass
    # print(fetch_last_index(DATA_DIR / "data_preview_1.jsonl"))
