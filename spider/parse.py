import urllib.parse

url = 'http://www.baidu.com/index.html;abc?m=1&n=xyz#opq'
res = urllib.parse.urlparse(url)
print(res)
print(res[0], res.scheme)

res = urllib.parse.urlsplit(url)
print(res)

unparse = ('http', 'www.baidu.com', 'index.html', 'abc', 'm=1&n=xyz', 'opq')
new_url = urllib.parse.urlunparse(unparse)
print(new_url == url)

unsplit = ['http', 'www.baidu.com', 'index.html;abc', 'm=1&n=xyz', 'opq']
new_url = urllib.parse.urlunsplit(unsplit)
print(new_url == url)

print(urllib.parse.urljoin('http://www.abc.com/abc.html', 'xyz.html'))
print(urllib.parse.urljoin('http://www.abc.com/a/b/c/abc.html', 'xyz.html'))
print(urllib.parse.urljoin('http://www.abc.com/a/b/c/abc.html', '../xyz.html'))
print(
    urllib.parse.urljoin('http://www.abc.com/a/b/c/abc.html',
                         '../../xyz.html'))
print(
    urllib.parse.urljoin('http://www.abc.com/a/b/c/abc.html',
                         '../../../xyz.html'))

data = {'a': 1, 'b': 2}
data = urllib.parse.urlencode(data)
print(data)

print(urllib.parse.parse_qs(data))
print(urllib.parse.parse_qsl(data))

chs = '你好'
chr_chs = urllib.parse.quote(chs)
chs = urllib.parse.unquote(chr_chs)
print(chr_chs, chs, sep='\n')
