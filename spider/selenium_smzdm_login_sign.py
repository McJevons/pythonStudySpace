from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
chrome_options.add_experimental_option("prefs", prefs)

browser = webdriver.Chrome(chrome_options=chrome_options)
browser.get('http://www.smzdm.com')

button_login = browser.find_element_by_class_name('J_login_trigger')
button_login.click()

browser.switch_to_frame('J_login_iframe')
username = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')
username.send_keys('jewely@qq.com')
password.send_keys('******')
button_submit = browser.find_element_by_id('login_submit')
button_submit.click()

browser.implicitly_wait(10)
sign_button = browser.find_element_by_class_name('J_punch')
sign_button.click()
