import urllib.request as request
import urllib.error as error
import urllib.parse as parse

headers_info = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
}

form_data = {
    'username': '18610991650',
    'password': '123456',
    'back': 'http%3A%2F%2Fhm.com%2FMain%2Findex.html'
}

proxy = {
    'http': '118.31.220.3:8080'
}

try:
    data = parse.urlencode(form_data).encode('utf8')
    res = request.Request('http://haomei.hylanda.com', data=data, headers=headers_info)
    # 使用ProxyHandle方法生成处理器对象
    proxy_handler = request.ProxyHandler(proxy)
    # 创建代理IP的opener实例
    opener = request.build_opener(proxy_handler)
    # html = opener.open(res).read().decode('utf8')
    html = opener.open(res)
    # html = request.urlopen(res).read().decode('utf8')
    print(html.info())
except error.URLError as e:
    if hasattr(e, 'reason'):
        print('error reason is '+str(e.reason))
except error.HTTPError as e:
    if hasattr(e, 'code'):
        print('error code is '+str(e.reason))
else:
    print('request success!')
