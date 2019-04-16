# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-16 11:38 
@mail: axingfly@gmail.com

Less is more.
"""

from flask import Flask
from flask_caching import Cache
from flask_cors import CORS

# 缓存
music_cache = Cache()


def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config.secure")
    app.config.from_object("app.config.setting")
    use_cache(app)
    register_blueprint(app)
    apply_cors(app)

    return app


def register_blueprint(app):
    from app.api import music_api
    app.register_blueprint(music_api, url_prefix='/v3/api')


def use_cache(app):
    music_cache.init_app(app, config=app.config['CACHE_CONFIG'])


def apply_cors(app):
    CORS(app)
