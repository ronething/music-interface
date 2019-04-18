# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-16 18:49 
@mail: axingfly@gmail.com

Less is more.
"""
from flask import jsonify, request, current_app

from app.api import music_api
from app import music_cache
import logging

from app.libs.exc import APIException
from app.libs.music import Music
from app.libs.utils import json_formatter, decode_bs64, auto_logging


@music_api.route('')
@music_cache.cached(timeout=3600 * 12)
def home():
    logging.debug('首次进入')
    return '<center><h3>立志登月，即使失之交臂，你也将着陆于星辰之间。</h3></center>'


@music_api.route('/slider')
def slider():
    logging.debug('首页轮播图')
    with auto_logging():
        slider = get_recommend()['data']['slider']
    music_slider = json_formatter(slider)
    return jsonify(music_slider)


@music_api.route('/hot')
def hot_list():
    logging.debug('热门歌单')
    with auto_logging():
        hot = get_recommend()['data']['songList']
    music_hot = json_formatter(hot)
    return jsonify(music_hot)


@music_api.route('/top')
@music_cache.cached()
def top_list():
    logging.debug('排行榜')
    music = Music()
    with auto_logging():
        res = music._top_list()
        if res['code'] != current_app.config['ERROR_OK']: raise APIException()
        top = res['data']['topList']
    music_top = json_formatter(top)
    return jsonify(music_top)


@music_api.route('/top/<int:topid>')
@music_cache.cached(timeout=3600 * 4)
def top_list_songs(topid):
    logging.debug('排行榜歌曲')
    music = Music()
    with auto_logging():
        top_res = music._top_list_songs(topid)
        if top_res['code'] != current_app.config['ERROR_OK']: raise APIException()
        total = top_res['total_song_num']
        _top_info = top_res['topinfo']
        top_info = dict(
            name=_top_info['ListName'],
            info=_top_info['info'],
            pic=_top_info['pic_album'],
        )
        logging.debug(top_info)
        update_time = top_res['update_time']
        all_song = get_songlist(top_res['songlist'])
    music_top_list_songs = json_formatter(dict(total=total, top_info=top_info,
                                               update_time=update_time, all_song=all_song))
    return jsonify(music_top_list_songs)


@music_api.route('/hotkeys')
@music_cache.cached()
def hot_keys():
    logging.debug('热门搜索')
    music = Music()
    with auto_logging():
        res = music._hot_keys()
        if res['code'] != current_app.config['ERROR_OK']: raise APIException()
        keys = res['data']
    music_hot_keys = json_formatter(keys)
    return jsonify(music_hot_keys)


@music_api.route('/search/<string:keyword>')
@music_cache.cached(timeout=3600, query_string=True)
def search_song(keyword):
    logging.debug('搜索歌曲')
    music = Music()
    with auto_logging():
        page = int(request.args.get('page', 1))
        count = int(request.args.get('count', 20))
        res = music._search(keyword, page, count)
        if res['code'] != current_app.config['ERROR_OK']: raise APIException()
        search = res['data']['song']
        total = search['totalnum']
        all_song = get_songlist(search['list'])
    music_search = json_formatter(dict(total=total, song=all_song))
    return jsonify(music_search)


@music_api.route('/lyric/<string:id>')
@music_cache.cached()
def song_lyric(id):
    logging.debug('获取歌词')
    music = Music()
    with auto_logging():
        res = music._lyric(id)
        if res['code'] != current_app.config['ERROR_OK']: raise APIException()
        lyc = decode_bs64(res['lyric'])
    music_lyc = json_formatter(dict(songid=id, lyric=lyc))
    return jsonify(music_lyc)


@music_api.route('/singer/pic/<string:mid>')
@music_cache.cached(timeout=3600 * 12)
def singer_ava(mid):
    logging.debug('获取歌手头像')
    music = Music()
    with auto_logging():
        res = music._singer_avatar(mid)
    singer_avatar = json_formatter(res)
    return jsonify(singer_avatar)


@music_api.route('/album/pic/<string:mid>')
@music_cache.cached(timeout=3600 * 12)
def album_ava(mid):
    logging.debug('获取专辑封面')
    music = Music()
    with auto_logging():
        res = music._album_pic(mid)
    album_pic = json_formatter(res)
    return jsonify(album_pic)


@music_api.route('/songs/url')
@music_cache.cached(timeout=60, query_string=True)
def songs_url():
    logging.debug('获取歌曲url')
    music = Music()
    with auto_logging():
        mids = request.args.get('songsmid', None)
        if mids is None: return APIException()
        res = music._songs_urls(mids)
    songs_meta = json_formatter(res)
    return jsonify(songs_meta)


@music_cache.cached()
def get_recommend():
    logging.debug('首页推荐条目')
    music = Music()
    with auto_logging():
        res = music._recommend()
        logging.debug(res)
        if res['code'] != current_app.config['ERROR_OK']: raise APIException()
    return res


def get_songlist(data):
    """解析歌曲列表数据"""
    all_song = []
    for m in data:
        # toplist 的 songlist 每个元素中有 data 但是 search 就没有 所以做一下判断
        if m.get('data') is not None: m = m['data']
        all_song.append(dict(
            albumid=m['albumid'],
            albummid=m['albummid'],
            albumname=m['albumname'],
            singer=[{'id': i['id'], 'mid': i['mid'], 'name': i['name']} for i in m['singer']],
            songname=m['songname'],
            songmid=m['songmid'],
            songid=m['songid'],
        ))
    return all_song
