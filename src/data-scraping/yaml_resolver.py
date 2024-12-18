import yaml
from pathlib import Path

def yaml_resolver():
    default_path = Path(__file__).parent / "element-xpaths" / "element-xpath.yaml"
    if default_path.exists():
        return default_path
    else:
        raise FileNotFoundError("Sorry! The original xpath data is redacted for ethical purposes!")


with open(yaml_resolver()) as elements_xpath:
    XPATH_DATA = yaml.safe_load(elements_xpath)