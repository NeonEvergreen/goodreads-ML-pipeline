# import json
# from itemadapter import ItemAdapter

# class JsonItemWriter():

#     def open_spider(self, spider):
#         self.file = open("./data/data_preview_101.jsonl", "w") 
    
#     def close_spider(self, spider):
#         self.file.close()

#     def process_item(self, item, spider):
#         line = json.dumps(ItemAdapter(item).asdict()) + "\n"
#         self.file.write(line)
#         return item