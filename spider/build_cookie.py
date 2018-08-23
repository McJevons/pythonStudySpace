import urllib.request
import urllib.parse
import http.cookiejar

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar(filename)
# 若不需保存cookie文件则使用下面语句
# cookie = http.cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

data = bytes(
    urllib.parse.urlencode({
        'username': 'hlf',
        'pwd': 'hlf'
    }),
    encoding='utf-8')
response = opener.open(
    'http://www.sh-huasing.com/web10/online/login.asp', data=data)
print(response.read().decode('gb2312'))
cookie.save(ignore_discard=True, ignore_expires=True)
