import urllib.request as request
import urllib.error as error

res = request.urlopen('https://www.baidu.com')
data = res.read().decode('utf-8')

url = res.geturl()
headers = res.info()
status = res.getcode()

try:
    headers_info = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
        'Cache-Control': 'max-age=0'
    }
    req = request.Request('https://www.baidu.com', headers=headers_info)
    html = request.urlopen(req)
    result = html.read().decode('utf-8')
except error.URLError as e:
    if hasattr(e, 'reason'):
        print('error reason is' + str(e.reason))
except error.HTTPError as e:
    if hasattr(e, 'code'):
        print('error code is ' + str(e.code))
else:
    print('request success!')

# print(result)
