# -*- coding: utf-8 -*-

import url_manager
import html_downloader
import html_parser
import html_outputer

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
        self.urls.add_new_urls(new_urls)

        count = 1
        while self.urls.has_new_url():
            try:
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_cont = self.downloader.download(new_url)
                new_data = self.parser.parse_song(new_url, html_cont)
                self.outputer.collect_data(new_data)
                count += 1
            except Exception, e:
                print 'craw failed'
                print e
            # if count == 30:
            #     break

        data = self.outputer.output_html()
        return data


def my_function():
    obj_spider = SpiderMain()
    root_url = 'http://music.163.com/discover/toplist?id=19723756'
    # data = obj_spider.craw(root_url)
    # root_url = 'http://music.163.com/discover/toplist?id=1899724'
    data = obj_spider.craw(root_url)
    return data

if __name__ == '__main__':
    data = my_function()
