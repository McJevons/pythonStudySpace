import urllib.request
import urllib.parse
import http.cookiejar

filename = 'cookie.txt'
cookie = http.cookiejar.MozillaCookieJar()
cookie.load(filename, ignore_discard=True, ignore_expires=True)
print(cookie)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)

response = opener.open('http://www.sh-huasing.com/web10/online/welcome.asp')
print(response.read().decode('gb2312'))
# cookie.save(ignore_discard=True, ignore_expires=True)
