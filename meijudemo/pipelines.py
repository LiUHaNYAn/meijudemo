# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time

import pymysql


class MeijudemoPipeline(object):
    def __init__(self):
        self.filename = str(time.time())

    def process_item(self, item, spider):
        con = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="pytest", charset="utf8")
        cusor = con.cursor()
        cusor.execute("insert into tb_meiju_newest(title,type,tvname,updatetime)VALUES (%s,%s,%s,%s)",
                      (item["name"], item["type"], item["tvname"], item["updatetime"]))
        con.commit()

        with open(self.filename + ".txt", "a", encoding="utf8") as fp:
            fp.write("名称：%s；类型：%s；来源：%s\n" % (item["name"], item["type"], item["tvname"]))


class MeijuListPipeline(object):
    def process_item(self, item, spider):
        # con = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="pytest", charset="utf8")
        # cusor = con.cursor()
        with open("meiju.sql","a",encoding="utf8") as fp:
            sql= "insert into tb_tvseries(name,enname,tvname,status,hot,type,classid,imgurl,linkurl,year,referurl)VALUES ('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');\r\n"\
                 %(item["name"], item["englishName"], item["tvname"], item["status"], item["hot"], item["type"], item["classid"],item["imgurl"], item["href"], item["year"],item["referurl"])
            fp.write(sql)
        # cusor.execute(
        #     "insert into tb_tvseries(name,enname,tvname,status,hot,type,classid,imgurl,linkurl,year,referurl)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        #     (item["name"], item["englishName"], item["tvname"], item["status"], item["hot"], item["type"], item["classid"],
        #      item["imgurl"], item["href"], item["year"],item["referurl"]))
        # con.commit()
