import requests

url1 = 'http://www.sh-huasing.com/web10/online/login.asp'
url2 = 'http://www.sh-huasing.com/web10/online/welcome.asp'
data = {'username': 'hlf', 'pwd': 'hlf'}

r = requests.post(url1, data)
print(r.content.decode('gb2312'))  # 登陆状态
r = requests.get(url2)
print(r.content.decode('gb2312'))  # 请求其他页面，变成非登陆状态，原cookie未保留

s = requests.Session()  # session保持会话状态
r = s.post(url1, data)
print(r.content.decode('gb2312'))  # 登陆状态
r = s.get(url2)
print(r.content.decode('gb2312'))  # 请求其他页面，仍旧为登陆状态
