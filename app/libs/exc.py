# -*- coding:utf-8 _*-  
""" 
@author: ronething 
@time: 2019-04-17 14:39
@mail: axingfly@gmail.com

Less is more.
"""
from werkzeug.exceptions import HTTPException
import json


class APIException(HTTPException):
    code = 500
    data = (
        '服务出现错误'
    )

    def __init__(self, code=None, data=None):
        if code:
            self.code = code
        if data:
            self.data = data
        super().__init__(data, None)

    def get_body(self, environ=None):
        from app.libs.utils import json_formatter
        body = json_formatter(data=self.data, code=self.code)
        text = json.dumps(body)
        return text

    def get_headers(self, environ=None):
        return [("Content-Type", "application/json")]
