# -*- coding: utf-8 -*-

import url_manager
import html_downloader
import html_parser
import html_outputer
import MySQLdb
import re

_author__ = 'Lust'


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, root_url):
        html_cont = self.downloader.download(root_url)
        new_urls = self.parser.parse_toplist(html_cont)
        conn = MySQLdb.Connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='imooc', charset='utf8')
        cursor = conn.cursor()
        for i in new_urls:
            pattern = re.compile(r"/song\?id=(\d+)")
            match = pattern.search(i)
            print match.groups()[0]
            sql_insert = "INSERT INTO toplist(music_id) VALUES(%s)" % (match.groups()[0])
            try:
                cursor.execute(sql_insert)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()
        cursor.close()
        conn.close()
        return new_urls


def my_function():
    obj_spider = SpiderMain()
    root_url = 'http://music.163.com/discover/toplist?id=4395559'
    # data = obj_spider.craw(root_url)
    # root_url = 'http://music.163.com/discover/toplist?id=1899724'
    data = obj_spider.craw(root_url)
    return data

if __name__ == '__main__':
    data = my_function()
