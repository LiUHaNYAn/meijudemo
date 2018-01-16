# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MeijudemoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    type = scrapy.Field()
    tvname = scrapy.Field()
    updatetime = scrapy.Field()


class MeijuCartonItem(scrapy.Item):
    name = scrapy.Field()
    imgurl = scrapy.Field()
    englishName = scrapy.Field()
    tvname = scrapy.Field()
    status = scrapy.Field()
    hot = scrapy.Field()
    type = scrapy.Field()
    href=scrapy.Field()
    year=scrapy.Field()
    referurl=scrapy.Field()
    classid=scrapy.Field()
