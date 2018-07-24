#!/usr/bin/env python

# -*- coding: utf-8 -*-

import datetime
import urllib.request as request
import urllib.error as error
from urllib.request import quote
import re

now_date = datetime.datetime.now().strftime('%Y%m%d')
key = '自制护肤品店'
key = quote(key)

headers_info = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
    'Cache-Control': 'max-age=0'
}

for i in range(1, 5):
    print('正在抓取第['+str(i)+']页')
    page = (i-1)*20
    url = 'https://shopsearch.taobao.com/search?app=shopsearch&q='+key+'&js=1&initiative_id=staobaoz_'+now_date+'&ie=utf8&s='+str(page)

    try:
        req = request.Request(url, headers=headers_info)
        html = request.urlopen(req).read().decode('utf8')
        print(html)
        exit()
    except error.URLError as e:
        if hasattr(e, 'reason'):
            print('error reason is' + str(e.reason))
    except error.HTTPError as e:
        if hasattr(e, 'code'):
            print('error code is ' + str(e.code))
    else:
        print('抓取第['+str(i)+']页完成！')

