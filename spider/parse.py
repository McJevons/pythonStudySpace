import urllib.parse

url = 'http://www.baidu.com/index.html;abc?m=1&n=xyz#opq'
res = urllib.parse.urlparse(url)
print(res)
print(res[0], res.scheme)

res = urllib.parse.urlsplit(url)
print(res)
