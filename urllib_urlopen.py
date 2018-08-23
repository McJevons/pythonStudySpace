import urllib.request

data = bytes(urllib.parse.urlencode({'a': 1, 'b': 2}), encoding='utf-8')
url = 'http://www.sh-huasing.com/web10/online/login.asp'
req = urllib.request.Request(url, data=data, method='POST')
response = urllib.request.urlopen(req)
print(response.read().decode('gb2312'))
