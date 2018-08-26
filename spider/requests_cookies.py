import requests

# 获取并打印cookies
data = {'username': 'hlf', 'pwd': 'hlf'}
url = 'http://www.sh-huasing.com/web10/online/login.asp'
r = requests.post(url, data)
print(r.cookies)
for key, value in r.cookies.items():
    print(key, value)

# 通过浏览器工具获取一个已登录页面的cookies，并将其复制到header的cookie中，然后通过程序获取该页面，已经是登录状态
header = {
    'cookie':
    'ASPSESSIONIDSADCCSDC=OIJLNEHAAGOAIODKMBEPNMKJ; safedog-flow-item=A4D69E078D41749F9E2C1188F870B3B0; Hm_lvt_acde41943fa74f0fd4701ea8ac79b6e1=1534601966,1535262182; hsweb=cfs%5Fe=&xx=0&mainUser=&title=&logintimes=1579&jkfb=hx&hx=True&hxcfs=&import=&custom=&username=HLF&co=&isLogin=1&isAdmin=0; Hm_lpvt_acde41943fa74f0fd4701ea8ac79b6e1=1535262508',
    'Host':
    'www.sh-huasing.com',
    'User-Agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}
r = requests.get(
    'http://www.sh-huasing.com/web10/online/welcome.asp', headers=header)
print(r.content.decode('gb2312'))
print(r.cookies)

header = {
    'cookie':
    '_zap=1a4d2827-d77d-4504-841b-4eeeca8289fd; d_c0="ADCCMRlsZQyPTitawkSEWa8QM4Mo3o5Swwk=|1505744762"; q_c1=13c56d708b3641caa8b1ed65d095f23f|1508419611000|1504706308000; __utmv=51854390.100-1|2=registration_date=20130914=1^3=entry_date=20130914=1; q_c1=e7e674df37404b0cb6049654bc4fd531|1532841571000|1532841571000; _xsrf=AwUaWQguwTTX6k8ssqZ9qw7MvouPOFyR; capsion_ticket="2|1:0|10:1534245154|14:capsion_ticket|44:ZTk0MmYwMDdhYzI4NDQ2MDkyNjM4OThmM2UxNDhlZWU=|d8435fb16c92ded9643f8875c1a9b63f57d36c7af318cd5f5e449296c5ff8d5c"; z_c0="2|1:0|10:1534245155|4:z_c0|92:Mi4xVFZFWEFBQUFBQUFBTUlJeEdXeGxEQ1lBQUFCZ0FsVk5Jd2RnWEFDMUE3YUo2bHdHci1sOHhLQVJjM3o5R1Zfd2Z3|d8ddddc0b812985ca9ab7a8f633e69603e660e33fc759b4af305ef8327cf866f"; __utma=51854390.1349278542.1505744765.1514904427.1535254277.5; __utmc=51854390; __utmz=51854390.1535254277.5.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); tgw_l7_route=53d8274aa4a304c1aeff9b999b2aaa0a',
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}
r = requests.get('https://www.zhihu.com', headers=header)
print(r.content.decode())
print(r.cookies)
