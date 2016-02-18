# coding=utf-8
'Download tieba picture html'

import urllib
import re

_author__ = 'Lust'


def getHtml(url):
    page = urllib.urlopen(url)
    html = page.read()
    return html


def getImg(html):
    reg = r'src="(.+?\.jpg)" pic_ext'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    print 'number of imgs:' + str(len(imglist))
    x = 0
    for imgurl in imglist:
        urllib.urlretrieve(imgurl, r'..\..\data\tieba_img\%s.jpg' % x)
        x += 1
        print "img's NO." + str(x)

html = getHtml("http://tieba.baidu.com/p/2460150866")

getImg(html)
