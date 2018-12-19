# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs
import os

# class TestinfoPipeline(object):
#     def __init__(self):
#         self.file = codecs.open('data.json', 'wb', encoding='utf-8')
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + ',' + '\n'
#         self.file.write(line)
#         return item
#
#     def spider_closed(self, spider):
#         self.file.close()

# class TestinfoPipeline(object):
#      def __init__(self):
#          self.file = codecs.open('data.json', 'w', encoding='utf-8')
#      def process_item(self, item, spider):
#          line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#          self.file.write(line)
#          return item
#      def spider_closed(self, spider):
#          self.file.close()

#追加的方式存储JSON 数据

class TestinfoPipeline(object):
     def process_item(self, item, spider):
         base_dir = os.getcwd()
         filename = base_dir + '/data.json'

         with codecs.open(filename, 'a') as f:
             line = json.dumps(dict(item), ensure_ascii=False) + '\n'
             f.write(line)
         return item

