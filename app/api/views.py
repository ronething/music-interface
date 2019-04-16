# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-16 18:49 
@mail: axingfly@gmail.com

Less is more.
"""
from flask import jsonify, request

from app.api import music_api
from app import music_cache
import logging
from app.libs.music import Music
from app.libs.utils import json_formatter


@music_api.route('')
@music_cache.cached(timeout=3600 * 12)
def home():
    logging.debug('首次进入')
    return '<center><h3>立志登月，即使失之交臂，你也将着陆于星辰之间。</h3></center>'


@music_api.route('/slider')
def slider():
    logging.debug('首页轮播图')
    try:
        slider = get_recommend()['data']['slider']
    except Exception as e:
        logging.error(e)
        return json_formatter(code=500)
    music_slider = json_formatter(slider)
    return jsonify(music_slider)


@music_api.route('/hot')
def hot_list():
    logging.debug('热门歌单')
    try:
        hot = get_recommend()['data']['songList']
    except Exception as e:
        logging.error(e)
        return json_formatter(code=500)
    music_hot = json_formatter(hot)
    return jsonify(music_hot)


@music_api.route('/top')
@music_cache.cached()
def top_list():
    logging.debug('排行榜')
    music = Music()
    try:
        top = music._top_list()['data']['topList']
    except Exception as e:
        logging.error(e)
        return json_formatter(code=500)
    music_top = json_formatter(top)
    return jsonify(music_top)


@music_api.route('/hotkeys')
@music_cache.cached()
def hot_keys():
    logging.debug('热门搜索')
    music = Music()
    try:
        keys = music._hot_keys()['data']
    except Exception as e:
        logging.error(e)
        return json_formatter(code=500)
    music_hot_keys = json_formatter(keys)
    return jsonify(music_hot_keys)


@music_api.route('/search/<string:keyword>')
@music_cache.cached(timeout=3600, query_string=True)
def search_song(keyword):
    logging.debug('搜索歌曲')
    music = Music()
    try:
        page = int(request.args.get('page', 1))
        count = int(request.args.get('count', 20))
        search = music._search(keyword, page, count)['data']['song']
        total = search['totalnum']
        all_song = []
        for m in search['list']:
            all_song.append(dict(
                albumid=m['albumid'],
                albummid=m['albummid'],
                albumname=m['albumname'],
                singer=[{'id': i['id'], 'mid': i['mid'], 'name': i['name']} for i in m['singer']],
                songname=m['songname'],
                songmid=m['songmid'],
            ))
    except Exception as e:
        logging.error(e)
        return json_formatter(code=500)
    music_search = json_formatter(dict(total=total, song=all_song))
    return jsonify(music_search)


@music_cache.cached()
def get_recommend():
    logging.debug('首页推荐条目')
    music = Music()
    res = music._recommend()
    return res
