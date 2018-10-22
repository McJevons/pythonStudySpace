from pyquery import PyQuery as pq
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)
bws = webdriver.Chrome(chrome_options=chrome_options)

song_name = '我一个人住'
url = 'https://music.163.com/#/search/m/?s=%s&type=1' % song_name
bws.get(url)
bws.switch_to.frame('contentFrame')
doc = pq(bws.page_source, parser="html")
with open('music163.html', 'w', encoding='utf-8') as file:
    file.write(bws.page_source)

with open('music163.html', 'r', encoding='utf-8') as file:
    html = file.read()
doc = pq(html, parser="html")
items = doc('.td.w0 a').items()
print(type(items))
for item in items:
    print(item.attr('href'))
    print(type(item))

# 切换回父frame才能关闭浏览器
# bws.switch_to.parent_frame
# bws.quit()
