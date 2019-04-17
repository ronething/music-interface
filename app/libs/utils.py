# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-16 17:48 
@mail: axingfly@gmail.com

Less is more.
"""

import json
import re
import base64
from contextlib import contextmanager
import logging
import traceback

from app.libs.exc import APIException


def json_formatter(data=None, code=0):
    """加工返回数据"""
    announce = '本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~'

    return dict(
        code=code,
        announce=announce,
        data=data,
    )


def loads_jsonp(jsonp_data):
    """解析jsonp数据格式为json"""
    try:
        return json.loads(re.match(".*?({.*}).*", jsonp_data, re.S).group(1))
    except:
        raise ValueError('Invalid Input')


def decode_bs64(bs64_data):
    """解密base64"""
    try:
        return base64.b64decode(bs64_data.encode('utf-8')).decode('utf-8')
    except:
        raise ValueError('Invalid Input')


@contextmanager
def auto_logging():
    try:
        yield
    except:
        logging.error(traceback.format_exc())
        raise APIException()
