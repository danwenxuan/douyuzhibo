# douyuzhibo
使用scrapy抓取斗鱼直播平台的信息
* 两种方式实现对斗鱼直播平台的信息抓取
* 方式一：在scrapy中的spider文件抓取所有图片的链接，然后在pipeline中使用urllib抓取图片
* 方式二：在scrapy中的抓取链接，在imagepipeline中，实现对图片的抓取
-----------------------------------------------------------------------
* git clone https://github.com/danwenxuan/douyuzhibo
* pip install scrapy
* python starts.py
