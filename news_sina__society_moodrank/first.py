# coding=utf-8

import re
from urllib import request

_author__ = 'lixintong'

# url = "http://news.sina.com.cn/society/moodrank/20161110.shtml"
url = "http://top.news.sina.com.cn/ws/GetTopDataList.php?top_type=day&top_cat=mood_moodnews1&top_time=20161110&top_show_num=8&top_order=DESC&short_title=1"

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
headers = {'User-Agent': user_agent}

# url_request = request.Request(url, headers=headers)
response = request.urlopen(url)

a = response.read()
b = str(a, encoding = "utf8").encode('utf-8').decode('unicode_escape')
print(b)