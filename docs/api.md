[TOC]

# 说明

-  均为 get 方法
- code 只为 0 或者 500 其中 0 表示成功，500 表示失败

## 首页轮播图

`v3/api/slider`

```json
// 20190417234353
// http://127.0.0.1:7000/v3/api/slider

{
  "announce": "本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~",
  "code": 0,
  "data": [
    {
      "id": 20667,
      "linkUrl": "https://y.qq.com/m/digitalbum/gold/index.html?openinqqmusic=1&_video=true&id=6605977&g_f=shoujijiaodian",
      "picUrl": "http://y.gtimg.cn/music/common/upload/MUSIC_FOCUS/1243375.jpg"
    },
    {
      "id": 20673,
      "linkUrl": "https://y.qq.com/m/act/sfhd/240.html?ADTAG=jdt",
      "picUrl": "http://y.gtimg.cn/music/common/upload/MUSIC_FOCUS/1243718.jpg"
    },
    ...
  ]
}
```

| 字段    | 字段说明 |
| ------- | -------- |
| linkUrl | 链接url  |
| picUrl  | 图片url  |

## 热门歌单

`v3/api/hot`

```json
// 20190417234755
// http://127.0.0.1:7000/v3/api/hot

{
  "announce": "本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~",
  "code": 0,
  "data": [
    {
      "accessnum": 10019356,
      "album_pic_mid": "",
      "id": "2646688496",
      "picUrl": "http://p.qpic.cn/music_cover/1Fr9IFMhWDPeUzWKVEjn3QTL2eX2QziaJmaL0ZAmsvtW71ic9IDUoYzg/300?n=1",
      "pic_mid": "00333So02drvak",
      "songListAuthor": "金青松",
      "songListDesc": "催泪大杀器！盘点演唱会经典万人大合唱"
    },
  	...
  ]
}
```

## 排行榜

`v3/api/top`

```json
// 20190417234950
// http://127.0.0.1:7000/v3/api/top

{
  "announce": "本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~",
  "code": 0,
  "data": [
    {
      "id": 4,
      "listenCount": 19600000,
      "picUrl": "http://y.gtimg.cn/music/photo_new/T003R300x300M000002zIokl2hVVpv.jpg",
      "songList": [
        {
          "singername": "吴青峰",
          "songname": "歌颂者"
        },
        {
          "singername": "毛不易",
          "songname": "东北民谣 (Live)"
        },
        {
          "singername": "李宇春",
          "songname": "你是人间的四月天"
        }
      ],
      "topTitle": "巅峰榜·流行指数",
      "type": 0
    },
    {
      "id": 26,
      "listenCount": 19100000,
      "picUrl": "http://y.gtimg.cn/music/photo_new/T003R300x300M000002suIku3wjAc9.jpg",
      "songList": [
        {
          "singername": "陈雪凝",
          "songname": "绿色"
        },
        {
          "singername": "摩登兄弟",
          "songname": "乞丐"
        },
        {
          "singername": "陈雪凝",
          "songname": "你的酒馆对我打了烊"
        }
      ],
      "topTitle": "巅峰榜·热歌",
      "type": 0
    },
    ...
  ]
}
```

## 排行榜歌曲

`v3/api/top/<int:topid>`

- topid 就排行榜的 id

```json
// 20190417235126
// http://127.0.0.1:7000/v3/api/top/26

{
  "announce": "本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~",
  "code": 0,
  "data": {
    "all_song": [
      {
        "albumid": 6271293,
        "albummid": "0010UePb4dyfoi",
        "albumname": "绿色",
        "singer": [
          {
            "id": 1473880,
            "mid": "004V53Ga0bV65j",
            "name": "陈雪凝"
          }
        ],
        "songid": 228849602,
        "songmid": "0021rBlZ1gQiLy",
        "songname": "绿色"
      },
      {
        "albumid": 6574807,
        "albummid": "000hdbrF4bBN6r",
        "albumname": "乞丐",
        "singer": [
          {
            "id": 1005787,
            "mid": "001KH1tJ02U8KY",
            "name": "摩登兄弟"
          }
        ],
        "songid": 230956311,
        "songmid": "002NMnL20hPR6W",
        "songname": "乞丐"
      },
      ...
    ],
    "top_info": {
      "info": "一周最具人气歌曲排行榜，旨在体现QQ音乐用户每周播放热度变更，为你展示当下热门优质有单曲循环价值的歌曲。<br><br>更新时间：每周四更新<br>排名数量：300首<br>统计算法：QQ音乐库内所有歌曲，根据综合数据7天前的涨幅进行排序，取前300名<br>综合数据：登录用户在QQ音乐播放/分享/下载数据",
      "name": "巅峰榜·热歌",
      "pic": "http://imgcache.qq.com/music/photo_new/T002R300x300M0000010UePb4dyfoi.jpg"
    },
    "total": 300,
    "update_time": "2019-04-11"
  }
}
```

## 热门搜索

- 关键字

`v3/api/hotkeys`

```json
// 20190417235308
// http://127.0.0.1:7000/v3/api/hotkeys

{
  "announce": "本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~",
  "code": 0,
  "data": {
    "hotkey": [
      {
        "k": "歌颂者 ",
        "n": 169334
      },
      {
        "k": "不在 ",
        "n": 46542
      },
      ...
    ],
    "special_key": "这就是原创",
    "special_url": "https://y.qq.com/m/act/yuanchuang2019/index.html?openinqqmusic=1&ADTAG=sousuoyunyingci&channelID=10032187"
  }
}
```

## 搜索歌曲

`v3/api/search/<string:keyword>`

- 可选参数 
- `page` 默认 1
- `count` 默认 20

```json
// 20190417235458
// http://127.0.0.1:7000/v3/api/search/%E8%AF%B4%E8%B0%8E?page=1&count=2

{
  "announce": "本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~",
  "code": 0,
  "data": {
    "song": [
      {
        "albumid": 303957,
        "albummid": "0046lmig2pi1M3",
        "albumname": "跨年演唱会2012-2013 华语篇2",
        "singer": [
          {
            "id": 11606,
            "mid": "001f0VyZ1hmWZ1",
            "name": "林宥嘉"
          }
        ],
        "songid": 3587123,
        "songmid": "003rSsgI26dTtu",
        "songname": "说谎 (Live)"
      },
      {
        "albumid": 2129666,
        "albummid": "003KNM2I0euFNa",
        "albumname": "超强音浪 第8期",
        "singer": [
          {
            "id": 5062,
            "mid": "002J4UUk29y8BY",
            "name": "薛之谦"
          }
        ],
        "songid": 201040703,
        "songmid": "004PTqgl1ctBPM",
        "songname": "说谎 (Live)"
      }
    ],
    "total": 398
  }
}
```

## 获取歌词

`v3/api/lyric/<string:id>`

- id: 歌曲 songid

```json
// 20190418000011
// http://127.0.0.1:7000/v3/api/lyric/3587123

{
  "announce": "本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~",
  "code": 0,
  "data": {
    "lyric": "[ti:说谎]\n[ar:林宥嘉]\n[al:跨年演唱会2012-2013 华语篇2]\n[by:]\n[offset:0]\n[00:01.02]说谎 (Live) - 林宥嘉 (Yoga Lin)\n[00:03.39]作词：施人诚\n[00:05.70]作曲 : 李双飞\n[00:08.26]\n[00:22.21]我好久没来这间餐厅\n[00:29.06]没想到已经换了装潢\n[00:35.69]角落那窗口 闻得到玫瑰花香\n[00:43.11]被你一说是有些印象\n[00:49.67]我没有说谎 我何必说谎\n[00:57.22]你知道的 我缺点之一就是很健忘\n[01:04.57]我哪有说谎 是很感谢今晚的相伴\n[01:13.05]但我竟然有些不习惯\n[01:19.68]\n[01:20.30]我没有说谎 我何必说谎\n[01:27.17]爱一个人 没爱到难道就会怎么样\n[01:34.66]别说我说谎 人生已经如此的艰难\n[01:43.02]有些事情就不要拆穿\n[01:49.51]我没有说谎 是爱情说谎\n[01:57.01]它带你来 骗我说 渴望的有可能有希望\n[02:04.83]我没有说谎 祝你做个幸福的新娘\n[02:19.19]\n[02:29.61]我的心事请你就遗忘",
    "songid": "3587123"
  }
}
```

## 获取歌手头像

`v3/api//singer/pic/<string:mid>`

- mid 歌手 singermid

```json
// 20190418000342
// http://127.0.0.1:7000/v3/api/singer/pic/003XriCI0123123123

{
  "announce": "本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~",
  "code": 0,
  "data": "https://y.gtimg.cn/music/photo_new/T001R300x300M000003XriCI0123123123.jpg?max_age=2592000"
}
```

## 获取专辑封面

`v3/api/album/pic/<string:mid>`

- mid 封面 albummid

```json
// 20190418000439
// http://127.0.0.1:7000/v3/api/album/pic/000Zdvra1EWgox

{
  "announce": "本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~",
  "code": 0,
  "data": "https://y.gtimg.cn/music/photo_new/T002R300x300M000000Zdvra1EWgox.jpg?max_age=2592000"
}
```

## 获取歌曲 URL

`v3/api/songs/url`

- 参数说明 `?songsmid=aa,bbb` 使用英文逗号隔开 ⚠️ 是 songmid 不是 songid

```json
// 20190418000828
// http://127.0.0.1:7000/v3/api/songs/url?songsmid=001hiWC00ii44N,001fg2pE0sy1B8

{
  "announce": "本接口所有数据均来自 qq 音乐, 仅供学习交流之用,请不要用于商业用途. 如果喜欢请下载 qq 音乐 app 畅听.如有侵权请联系 axingfly#gmail.com (#->@), 本人会进行删除等一系列相关操作~",
  "code": 0,
  "data": [
    {
      "001hiWC00ii44N": [
        "http://dl.stream.qqmusic.qq.com/M500001hiWC00ii44N.mp3?vkey=D66B01B5F7B058F16F22140E04B5053614343EEC9C3E6AB163DEA4D9C488247F983ECB1479D9433B590808C58AA59417E5654B3A05074654&guid=1204108538&fromtag=1",
        "http://dl.stream.qqmusic.qq.com/C400001hiWC00ii44N.m4a?vkey=D66B01B5F7B058F16F22140E04B5053614343EEC9C3E6AB163DEA4D9C488247F983ECB1479D9433B590808C58AA59417E5654B3A05074654&guid=1204108538&fromtag=1"
      ]
    },
    {
      "001fg2pE0sy1B8": [
        "http://dl.stream.qqmusic.qq.com/M500001fg2pE0sy1B8.mp3?vkey=D66B01B5F7B058F16F22140E04B5053614343EEC9C3E6AB163DEA4D9C488247F983ECB1479D9433B590808C58AA59417E5654B3A05074654&guid=1204108538&fromtag=1",
        "http://dl.stream.qqmusic.qq.com/C400001fg2pE0sy1B8.m4a?vkey=D66B01B5F7B058F16F22140E04B5053614343EEC9C3E6AB163DEA4D9C488247F983ECB1479D9433B590808C58AA59417E5654B3A05074654&guid=1204108538&fromtag=1"
      ]
    }
  ]
}
```

