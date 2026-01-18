## python packages
import string
## External dependencies
from yaml_resolver import XPATH_DATA
## Scrapy stuff
import scrapy
import itemloaders
from itemloaders.processors import MapCompose


def numeric_formatting(numeric_string : str) -> float:  # removing special characters (for reviews/ratings etc)
    try:
        return float(numeric_string.translate(
            str.maketrans("","",string.punctuation.replace(".","")) # avoid removing decimal point
            )) # str.maketrans(<replace this>, <with this>, <delete these>)
    except ValueError as e:
        raise ValueError(f"{__name__} :: Numeric Formatting failed :: {numeric_string} :: {e}")
    

def generate_data_page_schema()-> scrapy.Item: # We generate and return a custom scrapy Item based on yaml schema
    class DataPageSchema(scrapy.Item): #initialising a custom ITEM class
        pass

    DataPageSchema.fields["index"] = scrapy.Field() # Adding the Goodreads index field 

    for data_key_, data_dict in XPATH_DATA["data_pages"].items():  #Adding fields dynamically
        for data_label in data_dict["data_labels"]:
            DataPageSchema.fields[data_label] = scrapy.Field()    
    return DataPageSchema


def data_formatter(data_type, data):
    if data in [None, "", " "]: # if empty
        return data
    elif data_type == "int":  # integer
        return int(numeric_formatting(data))
    elif data_type == "float": # float
        return numeric_formatting(data)
    elif data_type == "str": # float
        return data.strip()
    else:
        return data # IMPORTANT for List & Unhandled data
    

def data_formatter_loader(data_labels : list, data_list : list, data_types : list, loader : itemloaders.ItemLoader)->itemloaders.ItemLoader:

    try:
        if "list" in data_types:
            loader.add_value(field_name=data_labels[0], value=data_list)
            return loader
        else:
            for label_, data_, type_ in zip(data_labels,data_list,data_types):
                formatted_data = data_formatter(data_type=type_, data=data_)
                loader.add_value(field_name=label_, value=formatted_data)
            return loader
    except Exception as e:
        raise Exception(f"{__name__} :: data Formatter failed :: {zip(data_labels,data_list,data_types)} :: {loader}")



if __name__ == "__main__":
    print(generate_data_page_schema().fields)
    print(data_formatter(data="$2,345.22", data_type="int"))