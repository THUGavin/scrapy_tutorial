# -*- coding: utf-8 -*-
import scrapy


class BdSpider(scrapy.Spider):
    name = "bd"
    allowed_domains = ["baidu.com"]
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print(response.css("title::text").extract())
