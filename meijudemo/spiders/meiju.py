# -*- coding: utf-8 -*-
import scrapy

from meijudemo.items import MeijudemoItem


class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['http://www.meijutt.com/new100.html']
    def parse(self, response):
        movies=response.xpath("//ul[@class='top-list  fn-clear']/li")
        item=MeijudemoItem()
        for movie in movies:
            item["name"]=movie.xpath("h5/a/text()").extract()[0]
            item["type"]=movie.xpath("span[@class='mjjq']/text()").extract()[0]
            item["tvname"]=movie.xpath("span[@class='mjtv']/text()").extract()[0]
            updatetimes1=movie.xpath("div[@class='lasted-time new100time fn-right']/text()").extract()
            updatetimes2=movie.xpath("div[@class='lasted-time new100time fn-right']/font/text()").extract()
            if updatetimes1.__len__()>0:
                item["updatetime"]=updatetimes1[0]
            if updatetimes2.__len__() > 0:
                item["updatetime"] = updatetimes2[0]
            yield item


