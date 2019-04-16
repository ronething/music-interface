# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-16 17:48 
@mail: axingfly@gmail.com

Less is more.
"""

from flask import Blueprint

music_api = Blueprint("api", __name__)

from . import views
