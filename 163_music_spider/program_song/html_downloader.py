# -*- coding: utf-8 -*-
import urllib2

_author__ = 'Lust'


class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            return None

        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64)'
        headers = {'User-Agent': user_agent}

        try:
            request = urllib2.Request(url, headers=headers)
            response = urllib2.urlopen(request)
            # print response.read().decode('UTF-8').encode('gbk', 'ignore')
        except urllib2.URLError, e:
            if hasattr(e, "code"):
                print e.code
            if hasattr(e, "reason"):
                print e.reason

        if response.getcode() != 200:
            return None
        html_content = response.read().decode('utf-8')
        return html_content
