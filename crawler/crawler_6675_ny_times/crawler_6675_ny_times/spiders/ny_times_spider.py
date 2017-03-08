# -*- coding:utf-8 -*-
import scrapy
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from crawler_6675_ny_times.items import Crawler6675NyTimesItem
import urllib
import time


def current_milli_time():
    return int(round(time.time() * 1000))


class ny_times_spider(CrawlSpider):
    name = "yuyangs_spider"
    start_time = current_milli_time()
    cur_time = start_time
    page_crawled = 0
    page_left = 1
    allowed_domains = ["nytimes.com"]
    start_urls = [
        "https://www.nytimes.com/"
    ]

    def parse(self, response):
        # a page has been crawled
        self.page_left -= 1
        self.page_crawled += 1

        selector = Selector(response)
        article_info_header = selector.xpath('//header[@id="story-header"]')

        item = Crawler6675NyTimesItem()
        item['is_article'] = 'N'
        item['url'] = response.url

        # if this page is a article
        if article_info_header:
            title = article_info_header.xpath('//h1[@id="headline"]/text()').extract()
            dates = article_info_header.xpath('//time[@class="dateline"]/text()').extract()
            date = dates[0]
            specialization = article_info_header.xpath('//a[@class="byline-column-link"]/text()').extract()
            author = article_info_header.xpath('//span[@class="byline-author"]/text()').extract()

            if 0 == len(author):
                author = article_info_header.xpath('//span[@class="byline-author "]/text()').extract()

            item['title'] = title
            item['date'] = date
            item['specialization'] = specialization
            item['author'] = author
            item['is_article'] = 'Y'

        other_links = selector.xpath('//a[@class="story-link"]/@href').extract()
        item['new_links_added'] = 0
        if other_links:
            new_pages = len(other_links)
            item['new_links_added'] = new_pages
            self.page_left += new_pages
            for link in other_links:
                if link:
                    yield Request(link, callback=self.parse)

        self.cur_time = current_milli_time()
        item['cur_time'] = (self.cur_time - self.start_time) / 1000
        item['pages_crawled'] = self.page_crawled
        item['pages_left'] = self.page_left
        yield item
