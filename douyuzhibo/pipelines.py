# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import urllib
import urllib.request
class DouyuzhiboPipeline(object):
    def process_item(self, item, spider):
        print(item['imagelink'])
        templist = item["imagelink"].split("/")
        print(templist[len(templist)-1])
        urllib.request.urlretrieve(item["imagelink"], "pic/" + templist[len(templist) - 1])
        return item
