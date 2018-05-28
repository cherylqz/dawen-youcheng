patenthub
==

### *支持python3.6


### *使用：

1、首先进入patenthub目录下运行proxies.py文件（终端命令：python3 proxies.py）；

2、生成proxies.txt文件后，运行spider下的patents.py文件(终端命令：scrapy crawl patents -o wenjianming.csv);

此处只抓取了一个免费代理网站上的ip，开源免费代理api(已fork)请参考jhao104/proxy_pool（https://github.com/jhao104/proxy_pool）

缺点：免费代理ip非常不稳定，建议用patents_selenium抓取

patents_selenium
==

### *基于selenium+chrome爬取专利信息，支持python3.6

### *使用：

直接运行即可（终端命令：python3 patents_selenium.py）

优缺点：能比较稳定的爬取，不容易被封ip，但是爬取的数量太多，会封掉账户
