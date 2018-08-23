import urllib.request

url = 'http://www.sh-huasing.com/web10'
response = urllib.request.urlopen(url)
print(response.read().decode('gb2312'))
