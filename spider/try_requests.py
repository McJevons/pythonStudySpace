import requests

# get测试，分类列出所有内容
r = requests.get('https://www.baidu.com/')
print(type(r._content))
for x in r.__attrs__:
    print(x, ':', type(eval('r.' + x)), ':', eval('r.' + x))

# 获取json格式测试
data = {'a': 1, 'b': 2}
r = requests.get('http://httpbin.org/get', data)
print(r.content.decode())
print(r.json())  # 将json字符串转为字典格式

# post登陆测试
data = {'username': 'hlf', 'pwd': 'hlf'}
url = 'http://www.sh-huasing.com/web10/online/login.asp'
r = requests.post(url, data)
print(r.content.decode('gb2312'))

# 抓取二进制数据，如图片
url = 'https://github.com/favicon.ico'
r = requests.get(url)
with open('./spider/images/favicon.ico', 'wb') as f:
    f.write(r.content)
