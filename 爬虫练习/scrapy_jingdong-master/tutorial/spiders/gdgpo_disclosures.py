#-*- encoding: UTF-8 -*-
#---------------------------------import------------------------------------
import scrapy
import re
from tutorial.items import ClassifyItem
from scrapy import Request
from scrapy.selector import Selector 
import json
import os, os.path 

#---------------------------------------------------------------------------
#广东采购公告
class gdgpoDisclosuresSpider(scrapy.Spider):
	name = "gdgpoDisclosuresSpider"
	allowed_domains = ["gdgpo.gov.cn"]
	
	def getlist():
		seq = []
		#2550
		for i in range(1000,2551):
			seq.append("http://www.gdgpo.gov.cn/queryMoreInfoList.do?channelCode=0008&pointPageIndexId=1&pageIndex="+str(i)+"&pageSize=15&pointPageIndexId=2")
		return seq;
		
	start_urls = getlist()

	def parse(self,response):
		""""""
		print(response.url)
		req = []
		for sel in response.xpath('//a[contains(@href, "showNotice")]'):
			for i in sel.xpath('@href').extract():
				url = "http://www.gdgpo.gov.cn" + i
				title = sel.xpath('@title').extract()[0]
				#print(url)
				r = Request(url, meta={'title': title}, callback=self.parse_details)
				req.append(r)
		return req
		
	def parse_details(self,response):
		""""""
		html = response.xpath('//div[@class="zw_contianer"]').extract()[0]
		#print(html)
		filepath = response.meta['title'] + '.html'
		opath = os.path.abspath("./广东中标结果/" + filepath) 
		basedir = os.path.dirname(opath) 
		if not os.path.exists(basedir): 
			os.makedirs(basedir) 
		#print(opath)
		with open(opath, 'w',encoding='utf-8') as f: 
			f.write(html)
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
