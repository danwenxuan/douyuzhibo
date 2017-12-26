# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DouyuzhiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name =scrapy.Field() #名称
    imagelink = scrapy.Field()#网络链接
    imagepath = scrapy.Field()#保存本地链接
    pass
