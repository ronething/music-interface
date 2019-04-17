# music-interface

## !!!

本接口仅用作学习交流之用, 请不要用在不正当手段。

## Introduction

- 最近在学一门课程 刚好需要某音乐网站的数据。so

## Development

在`app/config`下新建`secure.py`文件

```python
CACHE_CONFIG = {
    'DEBUG': True,
    'CACHE_TYPE': 'redis', # 可选类型参考 https://pythonhosted.org/Flask-Caching/#configuring-flask-caching
    'CACHE_DEFAULT_TIMEOUT': 300,
    'CACHE_REDIS_HOST': '127.0.0.1',
    'CACHE_REDIS_PORT': 6379,
    'CACHE_KEY_PREFIX': 'music_',
}
```

如果 `CACHE_TYPE` 选用 `redis` 需要本机启用一个 `redis` 服务

```
pipenv install
pipenv run python manage.py
```

## Deployment

- ~~暂时未部署 菜🐔~~
- 部署参考 [mp-music](https://github.com/ronething/mp-music)

## DEMO SITE

- 演示站点 [m.ronething.com](http://m.ronething.com/v3/api)
- ⚠️ 学生机一台经不起折腾 仅作为演示站点 随时关闭。

## API DOC

[doc](./docs/api.md)

## Acknowledgement

- [musicInterface](https://github.com/openSourceApi/musicInterface)
- [music-dl](https://github.com/0xHJK/music-dl)

## TODO

- [x] api doc

