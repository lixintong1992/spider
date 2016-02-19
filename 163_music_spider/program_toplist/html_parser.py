# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import re
import urlparse

_author__ = 'Lust'


class HtmlParser(object):

    def parse_toplist(self, html_cont):
        if html_cont is None:
            return
        song_url = 'http://music.163.com/song?id=399410728'
        soup = BeautifulSoup(html_cont, "lxml")
        new_urls = []
        song = soup.find_all('a', href=re.compile(r"/song\?id=\d+"))  # get songs_id

        for song_id in song:
            new_url = song_id['href']
            new_full_url = urlparse.urljoin(song_url, new_url)
            new_urls.append(new_full_url)
        return new_urls

#  bug to fix:1.can't recognition 2+ artists;                   done!
#             2.no id no artist/album directly write 'None'     done!
#             3.some music has both id_artist and no id_artist
    def parse_song(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont, "lxml")
        new_data = self._get_song_data(page_url, soup)
        return new_data

    def _get_song_data(self, page_url, soup):
        res_data = {}
        res_data['url'] = page_url

        song_name = soup.find_all('em', class_="f-ff2")[0].get_text()
        res_data['song_name'] = song_name

        res_data['song_artist_id'] = ''
        res_data['song_artist_name'] = ''
        # artist has id
        song_artist = soup.find_all('a', class_="s-fc7", href=re.compile(r"/artist\?id=\d+"))
        if len(song_artist) != 0:
            for i in song_artist:
                res_data['song_artist_id'] = res_data['song_artist_id'] + i['href'] + '$$'
                res_data['song_artist_name'] = res_data['song_artist_name'] + i.get_text() + '$$'
            res_data['song_artist_id'] = res_data['song_artist_id'][:-2]
        else:
            res_data['song_artist_id'] = 'None'
            print 'no artist_id!'
        # artist has no id
        song_artist_noid = soup.find_all('span', class_="s-fc7")
        if len(song_artist_noid) != 0:
            for i in song_artist_noid:
                res_data['song_artist_name'] = res_data['song_artist_name'] + i.get_text() + '$$'
        # make them format
        res_data['song_artist_name'] = res_data['song_artist_name'][:-2]

        song_album = soup.find_all('a', class_="s-fc7", href=re.compile(r"/album\?id=\d+"))
        if len(song_album) != 0:
            song_album_id = song_album[0]['href']
            song_album_name = song_album[0].get_text()
            res_data['song_album_id'] = song_album_id
            res_data['song_album_name'] = song_album_name
        else:
            res_data['song_album_id'] = 'None'
            res_data['song_album_name'] = 'None'
            print 'no song_album_id!'
        return res_data
