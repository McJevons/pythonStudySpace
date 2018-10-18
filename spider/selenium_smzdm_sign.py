from selenium import webdriver
import json

browser = webdriver.Chrome()
browser.get('http://www.smzdm.com')

# print(browser.get_cookies())

with open('cookie.txt', 'r') as file:
    cookies = json.load(file)

browser.delete_all_cookies()

for cookie in cookies:
    browser.add_cookie(cookie)

browser.refresh()

button = browser.find_element_by_class_name('J_punch')
button.click()
# browser.quit()
