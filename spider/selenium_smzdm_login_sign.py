from selenium import webdriver

browser = webdriver.Chrome()
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

