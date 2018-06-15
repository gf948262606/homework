# _*_ coding: utf-8 _*_

import scrapy
from scrapy.http import Request
from book.items import BookItem

class PhoneSpider(scrapy.Spider):
    name = 'book'
    allow_domins = ['dangdang.com']
    start_urls = ['http://3c.dangdang.com/mobile'] #初始化url

    def parse(self,response):
        #四类入口url
        category = response.xpath('//div[@class="level_one "]/dl/dt/a/@href').extract()
        #http://category.dangdang.com/all/?category_id=4004279
        category = [
                                'http://category.dangdang.com/cp51.00.00.00.00.00.html',
                                'http://category.dangdang.com/cp05.01.00.00.00.00.html',
                                'http://category.dangdang.com/cp05.02.00.00.00.00.html',
                                'http://category.dangdang.com/cp05.04.00.00.00.00.html',
                                'http://category.dangdang.com/cp05.06.00.00.00.00.html',
                                'http://category.dangdang.com/cp05.08.00.00.00.00.html',
                                'http://category.dangdang.com/cp05.10.00.00.00.00.html',
                                'http://category.dangdang.com/cp05.11.00.00.00.00.html',
                                #音乐
                                 'http://category.dangdang.com/all/?category_path=03.01.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.02.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.03.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.04.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.17.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.16.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.07.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.06.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.19.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.20.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.14.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.26.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.08.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.05.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.25.00.00.00.00.html',
                                 'http://category.dangdang.com/all/?category_path=03.21.00.00.00.00.html',
                                 'http://category.dangdang.com/cp03.13.00.00.00.00.html',
                                 'http://category.dangdang.com/cp03.09.00.00.00.00.html',
                                 'http://category.dangdang.com/cp03.10.00.00.00.00.html',
                                 'http://category.dangdang.com/cp03.24.00.00.00.00.html',
                                 'http://category.dangdang.com/cp03.23.00.00.00.00.html',
                                 'http://category.dangdang.com/cp03.15.00.00.00.00.html',
                                  'http://category.dangdang.com/cp03.18.00.00.00.00.html',
                                 'http://category.dangdang.com/cp03.27.00.00.00.00.html',
                                 'http://category.dangdang.com/cp03.12.00.00.00.00.html',
                                  #文具
                                'http://category.dangdang.com/cid10009416.html'
           			]


        for url in category:
            #print(url)
            #print('---------------------')
            yield Request(url, callback=self.parse_detail)

    def parse_detail(self, response):
        link = response.xpath('//a[@class="pic"]/@href').extract()
        next_link = response.xpath('//li[@class="next"]/a/@href')[0].extract()
        if next_link:
            yield Request('http://category.dangdang.com/'+next_link, callback=self.parse_detail)
        for detail_url in link:
            #print(detail_url)
            #print('+++++++++++++++++++++')
            yield Request(detail_url, callback=self.parse_price)

    def parse_price(self, response):
        item = BookItem()
        item['title'] = response.xpath('//div[@class="name_info"]/h1/@title').extract()
        item['comment_num'] = response.xpath('//a[@id="comm_num_down"]/text()').extract()
        item['link'] = response.url
        item['price'] = response.xpath('//p[@id="dd-price"]/text()').extract()[1]
        item['img_url'] = response.xpath('//img[@id="modalBigImg"]/@src').extract()
        item['cate_1'] = response.xpath('//div[@class="breadcrumb"]/a[@class="domain"]/b/text()').extract()
        item['cate_2'] = response.xpath('//div[@class="breadcrumb"]/a/text()').extract()[0]
        item['cate_3'] = response.xpath('//div[@class="breadcrumb"]/a/text()').extract()[1]
        yield item


