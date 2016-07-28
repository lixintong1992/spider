# coding=utf-8

import urllib2
from bs4 import BeautifulSoup
import re
import json

_author__ = 'Lust'


def download():
    url = 'http://news.sina.com.cn/s/wh/2016-05-11/doc-ifxryhhi8634318.shtml'  # content
    # url = 'http://comment5.news.sina.com.cn/count/info?key=comos-fxuaiwa6771008'  # comment
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
    html_content = response.read().decode('utf-8', 'ignore')
    # html_content = response.read().decode('gbk', 'ignore')
    # html_content = response
    return html_content


def toplist_parser(html_content):
    soup = BeautifulSoup(html_content, "lxml")

    song = soup.find_all('a', href=re.compile(r"/song\?id=\d+"))  # get songs_id
    song_id = song[0]['href']
    song_name = song.get_text()

    top_list = soup.find_all('a', class_="avatar", href=re.compile(r"/discover/toplist\?id=\d+"))
    toplist_id = top_list[0]['href']  # get toplist id
    toplist_name = top_list[0].img['alt']  # get toplist chinese name

    return song_id


def song_parser(html_content):
    soup = BeautifulSoup(html_content, "lxml")

    song_artist = soup.find_all('a', class_="s-fc7", href=re.compile(r"/artist\?id=\d+"))
    song_artist_id = song_artist[0]['href']
    song_artist_name = song_artist[0].get_text()

    song_album = soup.find_all('a', class_="s-fc7", href=re.compile(r"/album\?id=\d+"))
    song_album_id = song_album[0]['href']
    song_album_name = song_album[0].get_text()

    simil_song = soup.find_all('a', class_="s-fc1", href=re.compile(r"/song\?id=\d+"))  # 5
    simil_song_id = simil_song[0]['href']
    simil_song_name = simil_song[0]['title']

    person_likes = soup.find_all('a', class_="f-tdn", attrs={'data-res-action': "log"})  # 4
    person_likes_id = person_likes[0]['href']
    person_likes_name = person_likes[0]['title']


if __name__ == '__main__':
    html_content = download()
