#!/usr/bin/env python3
# -*- coding: utf8 -*-

import scrapy
class BrickSetSpider(scrapy.Spider):
    name = "brickset_spider"
    start_urls = ['http://brickset.com/sets/year-2016']

    def parse(self, response):
        SET_SELECTOR = '.set'
        for brickset in response.css(SET_SELECTOR):
            pass

            NAME_SELECTOR = 'h1 a ::text'
            yield {
                'name': brickset.css(NAME_SELECTOR).extract_first(),
            }