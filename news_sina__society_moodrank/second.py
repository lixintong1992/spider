# coding=utf-8

import re
from urllib import request

_author__ = 'lixintong'

# url = "http://news.sina.com.cn/society/moodrank/20161110.shtml"
# url = "http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=sh&newsid=comos-fxvixeq0401461&group=&compress=0&ie=gbk&oe=gbk&page=1&page_size=20&jsvar=loader_1541438280743_17470765"
url = "http://comment5.news.sina.com.cn/page/info?version=1&format=js&channel=sh&newsid=comos-fxvixeq0401461&group=&compress=0&ie=gbk&oe=gbk&page=1&page_size=20"

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
headers = {'User-Agent': user_agent}

# url_request = request.Request(url, headers=headers)
response = request.urlopen(url)

a = response.read()
b = str(a, encoding = "utf8").encode('utf-8').decode('unicode_escape')
print(b)