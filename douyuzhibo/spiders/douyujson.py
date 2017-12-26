# -*- coding: utf-8 -*-
import scrapy
from douyuzhibo.items import  DouyuzhiboItem
import json
class DouyujsonSpider(scrapy.Spider):
    name = 'douyujson'
    allowed_domains = ['capi.douyucdn.cn']
    offset=0
    start_urls = ['http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset=0']

    def parse(self, response):
        data=json.loads(response.text)["data"] #转化为json类型取出data字段
        for dataline  in data:
            ditem=DouyuzhiboItem()
            ditem["name"]=dataline["nickname"]
            ditem["imagelink"]=dataline["vertical_src"]
            yield ditem
        if self.offset <240:
            self.offset+=20
            yield scrapy.Request("http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="+str(self.offset),callback=self.parse)

