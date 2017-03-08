# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class Crawler6675NyTimesItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    author = scrapy.Field()
    date = scrapy.Field()
    specialization = scrapy.Field()
    url = scrapy.Field()
    new_links_added = scrapy.Field()
    is_article = scrapy.Field()
    cur_time = scrapy.Field()
    pages_left = scrapy.Field()
    pages_crawled = scrapy.Field()
