from selenium import webdriver

url = 'http://192.168.1.56:8750/#/site_data/detail'
# 初始化浏览器对象
browser = webdriver.Chrome()
# 向指定网址发起GET请求
browser.get(url)
# 使用CSS选择器定位按钮，并点击按钮
browser.find_element_by_css_selector('#app > div > div > div.web-login-right > form > button').click()
# 将按钮点击后的网页文本赋值给变量resp
resp = browser.page_source
print(resp)
# 程序退出，关闭浏览器
browser.quit()