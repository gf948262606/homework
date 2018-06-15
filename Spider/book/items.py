# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field()
    comment_num = scrapy.Field()
    link = scrapy.Field()
    img_url = scrapy.Field()
    cate_1 = scrapy.Field()
    cate_2 = scrapy.Field()
    cate_3 = scrapy.Field()
