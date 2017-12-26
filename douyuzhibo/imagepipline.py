#!usr/bin/python/
#-*-conding:utf-8-*-
import scrapy
from scrapy.utils.project  import get_project_settings
from scrapy.pipelines.images import ImagesPipeline
import os


class ImagePIPELINE(ImagesPipeline):
	Image_STORE = get_project_settings().get("IMAGES_STORE")  # 默认路径

	def get_media_requests(self, item, info):
		url = item["imagelink"]  # 自动下载
		yield scrapy.Request(url)  # 下载请求，自动调度

	def item_completed(self, result, item, info):
		# 下载到临时文件 reslut [( 下载成功,path),]
		image_path = [x["path"] for ok, x in result if ok]
		# 重命名
		os.rename(self.Image_STORE + "\\" + image_path[0], self.Image_STORE + "\\" + item["name"] + ".jpg")
		item["imagepath"] = self.Image_STORE + "\\" + item["name"] + ".jpg"

		return item