from selenium import webdriver
import json

# 设置chrome选项为不加载图像
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

# 根据chrome选项驱动开启浏览器
browser = webdriver.Chrome(chrome_options=chrome_options)
# 加载网页
browser.get('http://www.smzdm.com')

with open('cookies.txt', 'r') as file:
    cookies = json.load(file)

# 先清空原cookies，确保不受其他内容影响
browser.delete_all_cookies()

for cookie in cookies:
    browser.add_cookie(cookie)

# 刷新浏览器，使写入的cookies生效
browser.refresh()

button = browser.find_element_by_class_name('J_punch')
button.click()

browser.quit()
