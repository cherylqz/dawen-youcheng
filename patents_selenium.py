# -*- coding: utf-8 -*-
from selenium import webdriver
import time
import pandas as pd
import csv
import random

data = pd.read_excel('Namelist.xlsx')

browser=webdriver.Chrome()
url="https://www.patenthub.cn/"
browser.get(url)

time.sleep(3)

#进入登录页面，模拟登陆
browser.find_element_by_xpath("/html/body/nav/div[4]/a[2]").click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="account"]').send_keys('18101263125')
time.sleep(2)
browser.find_element_by_xpath('//*[@id="password"]').send_keys('zqr1997@')
time.sleep(2)
browser.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div[3]/button[1]").click()
time.sleep(3)

#检索公司
for j in range(len(data['name'])):
    browser.find_element_by_xpath('//*[@id="q"]').clear()
    browser.find_element_by_xpath('//*[@id="q"]').send_keys('(ap:"'+data['name'][j]+'") AND (dd:[2008-01-01 TO 2018-04-01])')
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="selection-dropdown"]/button').click()
    time.sleep(2)
    rows=[]
    
    #解析专利信息
    for i in range(100):
        try:
            items=browser.find_elements_by_xpath('//ul[@class="patent-bib"]')
            for i in range(len(items)):
                a=str(i+1).replace("'","")
                patent={
                    #'applicant':browser.find_element_by_xpath(str('//*[@id="mode_1"]/ul['+a+']/li/div/ul/li[7]/a/span/span')).text,
                    'applicant':data['name'][j],
                    'application_date':browser.find_element_by_xpath(str('//*[@id="mode_1"]/ul['+a+']/li/div/ul/li[6]/span')).text,
                    'application_number':browser.find_element_by_xpath(str('//*[@id="mode_1"]/ul['+a+']/li/div/ul/li[5]/span')).text,
                    'document_date':browser.find_element_by_xpath(str('//*[@id="mode_1"]/ul['+a+']/li/div/ul/li[4]/span')).text,
                    'title':browser.find_element_by_xpath(str('//*[@id="mode_1"]/ul['+a+']/li/div/ul/li[1]/div[2]/a[1]/span[2]')).text,
                    'document_number':browser.find_element_by_xpath(str('//*[@id="mode_1"]/ul['+a+']/li/div/ul/li[3]/span')).text,
                    'inventor':browser.find_element_by_xpath(str('//*[@id="mode_1"]/ul['+a+']/li/div/ul/li[8]/a[1]/span')).text,
                    'patenttag':browser.find_element_by_xpath(str('//*[@id="mode_1"]/ul['+a+']/li/div/ul/li[1]/div[2]/a[2]')).text
                }
                rows.append(patent)
            #翻页
            next_page=browser.find_element_by_xpath('//*[@id="search-list"]/div[2]/div/div[2]/div[1]/a[last()]').text
            if next_page=="下一页":
                browser.find_element_by_xpath('//*[@id="search-list"]/div[2]/div/div[2]/div[1]/a[last()]').click()
                time.sleep(random.randint(2,4))
            else:
                #将结果写入csv文件
                path='hs300patents.csv'
                headers=['applicant','application_date','application_number','document_date','title','document_number','inventor','patenttag']
                with open(path,'a')as f:
                    f_csv=csv.DictWriter(f,headers)
                    f_csv.writeheader()
                    f_csv.writerows(rows)
                break
    except:
        pass
