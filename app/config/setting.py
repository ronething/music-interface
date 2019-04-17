# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-16 17:44 
@mail: axingfly@gmail.com

Less is more.
"""

import os
from dotenv import load_dotenv
import logging

load_dotenv()

environ = os.getenv('FLASK_ENV', 'development')

PORT = 7000

if environ == 'production':

    DEBUG = False

    HOST = '0.0.0.0'

    logging.basicConfig(level=logging.ERROR)

else:

    DEBUG = True

    HOST = '127.0.0.1'

    logging.basicConfig(level=logging.DEBUG)

DF_DATA = {
    'g_tk': '5381',
    'uin': '0',
    'format': 'json',
    'inCharset': 'utf-8',
    'outCharset': 'utf-8',
    'notice': '0',
    'platform': 'h5',
    'needNewCode': '1',
    # '_': str(int(round(time.time() * 1000)))
}

DF_HEADERS = {
    'Accept': 'application/json',
    'Origin': 'https://y.qq.com',
    'Referer': 'https://y.qq.com/m/index.html',
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

QQ_MUSIC_COMMON_BASE_URL = 'https://c.y.qq.com'

ERROR_OK = 0
