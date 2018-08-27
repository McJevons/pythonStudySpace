import requests
from requests import Request, Session
from requests.packages import urllib3
from requests_oauthlib import OAuth1

# SSL验证，verify参数默认True，验证证书
# 12306没有证书，验证证书参数verify为True的时候会报错，因此设置为不验证证书
urllib3.disable_warnings()  # 屏蔽警告
response = requests.get('https://www.12306.cn', verify=False)
print(response.status_code)

# 代理设置
proxies = {
    "http": "http://10.10.1.10:3128",
    "https": "http://10.10.1.10:1080",
}
# 需要登录的代理
# proxies = {
#     "http": "http://user:password@10.10.1.10:3128/",
# }
# socks5代理，需安装socks库：pip3 install 'requests[socks]'
# proxies = {
#     'http': 'socks5://user:password@host:port',
#     'https': 'socks5://user:password@host:port'
# }
requests.get("https://www.taobao.com", proxies=proxies)

# 身份认证
r = requests.get('http://localhost:5000', auth=('username', 'password'))
print(r.status_code)

# OAuth认证，先安装oauth库：pip3 install requests_oauthlib
url = 'https://api.twitter.com/1.1/account/verify_credentials.json'
auth = OAuth1('YOUR_APP_KEY', 'YOUR_APP_SECRET', 'USER_OAUTH_TOKEN',
              'USER_OAUTH_TOKEN_SECRET')
requests.get(url, auth=auth)

# Prepared Request，所有参数都放在一个request里面
url = 'http://httpbin.org/post'
data = {'name': 'germey'}
headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36'
}
s = Session()
req = Request('POST', url, data=data, headers=headers)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
