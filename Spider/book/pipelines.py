# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BookPipeline(object):
    def process_item(self, item, spider):
        name = item['title'][0]
        comment_num = item['comment_num'][0]
        url = item['link']
        price=item['price']
        img_url = item['img_url'][0]
        kind = item['cate_1'][0]
        kind_2 = item['cate_2']
        kind_3 = item['cate_3']
        print (u'商品名：'+name)
        print (u'评论数:'+comment_num)
        print (u'商品链接：'+url)
        print (u'价格:'+price)
        print (u'图片链接:'+img_url)
        print (u'商品一级分类：'+kind)
        print (u'商品二级分类：'+kind_2)
        print (u'商品三级分类：'+kind_3)
        print('----------------')
        return item
