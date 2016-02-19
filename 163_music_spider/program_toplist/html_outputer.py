# -*- coding: utf-8 -*-
import re
import MySQLdb

_author__ = 'Lust'


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

#  bug to fix:1.many [0] in re , should be transfer into for structure
    def output_html(self):
        conn = MySQLdb.Connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='imooc', charset='utf8')
        cursor = conn.cursor()
        for data in self.datas:
            print data['url']
            pattern = re.compile(r"/song\?id=(\d+)")
            match = pattern.search(data['url'])
            print match.groups()[0]
            print data['song_name']

            sql_insert = "INSERT INTO music(music_id,music_name) VALUES(%s,\"%s\")" % (match.groups()[0], data['song_name'])
            try:
                cursor.execute(sql_insert)
                conn.commit()
            except Exception as e:
                print e
                conn.rollback()

            print data['song_artist_id']
            if data['song_artist_id'] != 'None':
                pattern = re.compile(r"/artist\?id=(\d+)")
                match = pattern.search(data['song_artist_id'])
                print match.groups()[0]
            print data['song_artist_name'].encode('gbk', 'ignore')

            print data['song_album_id']
            if data['song_album_id'] != 'None':
                pattern = re.compile(r"/album\?id=(\d+)")
                match = pattern.search(data['song_album_id'])
                print match.groups()[0]
            print data['song_album_name'].encode('gbk', 'ignore')
            print '\n'

        cursor.close()
        conn.close()
        return self.datas
