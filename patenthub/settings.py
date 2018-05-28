# -*- coding: utf-8 -*-

# Scrapy settings for patenthub project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

import random
BOT_NAME = 'patenthub'

SPIDER_MODULES = ['patenthub.spiders']
NEWSPIDER_MODULE = 'patenthub.spiders'


ROBOTSTXT_OBEY = False
COOKIES_ENABLED=False
REDIRECT_ENABLED=True

DOWNLOAD_DELAY=random.randint(3, 10)

# user agent 列表
USER_AGENT_LIST = [
                   'MSIE (MSIE 6.0; X11; Linux; i686) Opera 7.23',
                   'Opera/9.20 (Macintosh; Intel Mac OS X; U; en)',
                   'Opera/9.0 (Macintosh; PPC Mac OS X; U; en)',
                   'iTunes/9.0.3 (Macintosh; U; Intel Mac OS X 10_6_2; en-ca)',
                   'Mozilla/4.76 [en_jp] (X11; U; SunOS 5.8 sun4u)',
                   'iTunes/4.2 (Macintosh; U; PPC Mac OS X 10.2)',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:5.0) Gecko/20100101 Firefox/5.0',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0) Gecko/20100101 Firefox/9.0',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.8; rv:16.0) Gecko/20120813 Firefox/16.0',
                   'Mozilla/4.77 [en] (X11; I; IRIX;64 6.5 IP30)',
                   'Mozilla/4.8 [en] (X11; U; SunOS; 5.7 sun4u)'
                   ]
# 随机生成user agent
USER_AGENT = random.choice(USER_AGENT_LIST)

DOWNLOADER_MIDDLEWARES = {
    'patenthub.middlewares.ProxyMiddleWare': 100
}
