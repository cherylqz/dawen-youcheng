# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from patenthub.items import PatenthubItem
import pandas as pd
import urllib
import time
import random
import requests

class PatentsSpider(scrapy.Spider):
    name = 'patents'
    allowed_domains = ['www.patenthub.cn']
    start_urls = ['http://www.patenthub.cn/user/login.html']
    

    def parse(self, response):
        return scrapy.FormRequest.from_response(
                                                response,
                                                url='https://www.patenthub.cn/user/login.json',
                                                formdata={'account':'18101263125','password':'zqr1997@'},
                                                callback=self.after_login,
                                                dont_filter=True
                                                )


    def after_login(self,response):
        if b'authentication failed' in response.body:
            self.log("Login failed",level=log.ERROR)
            return
        else:
            data = pd.read_excel('Namelist.xlsx')
            urls=[]
            for i in range(50):   #for i in range(len(data['name'])):  可以获取seedfile里的全部股票
                url1="https://www.patenthub.cn/s?ds=cn&dm=mix&s=score%21&q=%28ap%3A%22"
                url2="%22%29+AND+%28dd%3A%5B2008-01-01+TO+2018-05-01%5D%29"
                urls.append(url1+urllib.parse.quote(data['name'][i])+url2)
            for url in urls:
                time.sleep(random.randint(2,5))
                yield Request(url,callback=self.parse_patentPage)

    def parse_patentPage(self,response):
        for patent in response.xpath('//ul[contains(@class,"ui items")]'):
            item = PatenthubItem()
            item['title']=patent.xpath('.//span[@data-property="title"]/text()').extract_first()
            item['document_number']=patent.xpath('.//span[@data-property="documentNumber"]/text()').extract_first()
            item['document_date']=patent.xpath('.//span[@data-property="documentDate"]/text()').extract_first()
            item['application_number']=patent.xpath('.//span[@data-property="applicationNumber"]/text()').extract_first()
            item['application_date']=patent.xpath('.//span[@data-property="applicationDate"]/text()').extract_first()
            item['applicant']=patent.xpath('.//span[@data-property="applicant"]/text()').extract_first()
            item['inventor']=patent.xpath('.//span[@data-property="inventor"]/text()').extract()
            item['patenttag']=patent.xpath('.//li/div/ul/li[1]/div[2]/a[2]/text()').extract()
            yield item
            time.sleep(random.randint(3,10))
            next_page=response.xpath('//div[@class="ui borderless pagination menu"]/a[@class="item"][last()]/@href').extract_first()
            if next_page:
                yield Request('https://www.patenthub.cn'+next_page,callback=self.parse_patentPage)


