# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-16 17:48 
@mail: axingfly@gmail.com

Less is more.
"""


def json_formatter(data=None, code=0):
    """加工返回数据"""
    announce = '本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~'

    return dict(
        code=code,
        announce=announce,
        data=data,
    )
