# -*- coding: utf-8 -*-
import scrapy

from meijudemo.items import MeijuCartonItem


class CartoonSpider(scrapy.Spider):
    name = 'cartoon'
    allowed_domains = ['www.meijutt.com']
    # start_urls = ['http://www.meijutt.com/file/list6.html']

    urls = []

    def start_requests(self):
        return [scrapy.Request("http://www.meijutt.com/file/list6.html", callback=self.getpager),
                scrapy.Request("http://www.meijutt.com/file/list5.html", callback=self.getpager),
                scrapy.Request("http://www.meijutt.com/file/list4.html", callback=self.getpager),
                scrapy.Request("http://www.meijutt.com/file/list3.html", callback=self.getpager),
                scrapy.Request("http://www.meijutt.com/file/list2.html", callback=self.getpager),
                scrapy.Request("http://www.meijutt.com/file/list1.html", callback=self.getpager)
                ]

    def getpager(self, response):
        val = response.xpath("//div[@class='page']/span/text()").extract()[0]
        pagenum = int(str(val).split("/")[1].split(" ")[0])
        classid = response.url.split('.html')[0][-1]
        yield self.make_requests_from_url(response.url)
        for i in range(pagenum):
            url = ("http://www.meijutt.com/file/list%s.html" % classid).replace(".html", "_" + str(i + 1) + ".html")
            yield self.make_requests_from_url(url)

    def parse(self, response):
        data = response.xpath("//div[@class='cn_box2']")
        url = str(response.url)
        classid=0
        if url.find("_")>0:
            classid = url.split("_")[0][-1]
        else:
            classid = url.split(".html")[0][-1]

        for item in data:
            it = MeijuCartonItem();
            it["name"] = item.xpath("div[@class='cn_box_box3']/div[@class='bor_img3_right']/a/@title").extract()[0];
            it["imgurl"] = item.xpath("div[@class='cn_box_box3']/div[@class='bor_img3_right']/a/img/@src").extract()[0]

            it["englishName"] = item.xpath("ul[@class='list_20']/li[2]/font[@class='cor_move_li']/text()").extract()[0]
            it["href"] = "http://www.meijutt.com/%s" % item.xpath("ul[@class='list_20']/li[1]/a/@href").extract()[0]
            it["tvname"] = item.xpath("ul[@class='list_20']/li[3]/font[@class='cor_move_li']/text()").extract()[0]
            it["status"] = item.xpath("ul[@class='list_20']/li[4]/span/font/text()").extract()[0]
            it["hot"] = item.xpath("ul[@class='list_20']/li[5]/font[@class='cor_move_li']/text()").extract()[0]
            it["year"] = item.xpath("ul[@class='list_20']/li[6]/font[@class='cor_move_li']/text()").extract()[0]
            it["referurl"] = url
            it["classid"] = classid
            try:
                it["type"] = item.xpath("ul[@class='list_20']/li[7]/font[@class='cor_move_li']/text()").extract()[0]
            except Exception  as ex:
                print(ex)
                it["type"] = ""
            yield it
