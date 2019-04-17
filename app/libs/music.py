# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-16 18:10 
@mail: axingfly@gmail.com

Less is more.
"""

import requests
from flask import current_app
import logging
import time
from app.libs.utils import loads_jsonp


class Music(object):

    def __init__(self):
        self.payload = current_app.config['DF_DATA']
        # 加上毫秒时间戳 不在这里初始化的话 时间戳会固定 暂时没想到其他方法
        self.payload['_'] = str(int(round(time.time() * 1000)))
        self.headers = current_app.config['DF_HEADERS']
        self.base_url = current_app.config['QQ_MUSIC_COMMON_BASE_URL']

    def _recommend(self):
        """首页推荐"""
        url = "{}/musichall/fcgi-bin/fcg_yqqhomepagerecommend.fcg".format(self.base_url)
        res = requests.get(url, params=self.payload, headers=self.headers)
        return res.json()

    def _top_list(self):
        """排行榜"""
        url = "{}/v8/fcg-bin/fcg_myqq_toplist.fcg".format(self.base_url)
        logging.debug(self.payload['_'])
        res = requests.get(url, params=self.payload, headers=self.headers)
        return res.json()

    def _top_list_songs(self, id):
        """排行榜中列表歌曲"""
        url = "{}/v8/fcg-bin/fcg_v8_toplist_cp.fcg".format(self.base_url)
        self.payload['topid'] = id
        res = requests.get(url, params=self.payload, headers=self.headers)
        return res.json()

    def _hot_keys(self):
        """热门搜索关键字"""
        url = "{}/splcloud/fcgi-bin/gethotkey.fcg".format(self.base_url)
        res = requests.get(url, params=self.payload, headers=self.headers)
        return res.json()

    def _search(self, keyword, page, count):
        """
        搜索歌曲
        :param keyword: 关键字
        :param page: 页码
        :param count: 每页数量
        :return:
        """
        url = "{}/soso/fcgi-bin/search_for_qq_cp".format(self.base_url)
        self.payload['w'] = keyword
        self.payload['p'] = page
        self.payload['n'] = count if count <= 20 else 20  # max 20
        res = requests.get(url, params=self.payload, headers=self.headers)
        return res.json()

    def _lyric(self, id):
        """获取歌词"""
        url = "{}/lyric/fcgi-bin/fcg_query_lyric.fcg".format(self.base_url)
        config = dict(
            musicid=id,
            nobase64=0,
            jsonpCallback='jsonp1'
        )
        self.payload.update(config)
        res = requests.get(url, params=self.payload, headers=self.headers)
        return loads_jsonp(res.text)

    def _singer_track(self):
        pass

    def _singer_avatar(self, mid):
        """歌手头像"""
        url = current_app.config['SINGER_AVATAR_BASE_URL'].format(mid)
        return url

    def _album_pic(self, mid):
        """专辑封面"""
        url = current_app.config['ALBUM_BASE_URL'].format(mid)
        return url
