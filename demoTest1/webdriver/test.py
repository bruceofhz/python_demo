# 从selenium里面导入webdriver
import time

from selenium import webdriver

# 指定chrom的驱动
# 执行到这里的时候Selenium会到指定的路径将chrome driver程序运行起来
driver = webdriver.Chrome('E:\chromedriver_win32\chromedriver.exe')
# driver = webdriver.Firefox()#这里是火狐的浏览器运行方法

# get 方法 打开指定网址
driver.get('http://192.168.1.56:8981/')

# 选择网页元素
element_user = driver.find_element_by_css_selector(
    '#root > div > div > div > form > div > div.saas_login_input_user___q0pFw > span > span > input')
element_pasword = driver.find_element_by_css_selector(
    '#root > div > div > div > form > div > div.saas_login_input_pasword___L1Kmq > span > span > input')

# 输入用户名和密码
element_user.send_keys('admin')
time.sleep(1)
element_pasword.send_keys('123456')

# 登录
element_search_button = driver.find_element_by_tag_name('button')
element_search_button.click()

time.sleep(1)

# 列表元素
goods = driver.find_element_by_css_selector(
    '#root > div > section > section > aside > div > ul > li:nth-child(3) > div.ant-menu-submenu-title > span > span')
goods.click()

goods = driver.find_element_by_css_selector(
    '#root > div > section > section > aside > div > ul > li:nth-child(4) > div.ant-menu-submenu-title > span > span')
goods.click()

goods = driver.find_element_by_css_selector(
    '#root > div > section > section > aside > div > ul > li:nth-child(11) > div.ant-menu-submenu-title')
goods.click()

li1 = driver.find_element_by_xpath('//*[@id="zyg_report$Menu"]/li[1]')

print(li1.text)
li1.click()

t1 = driver.find_element_by_css_selector(
    '#first_visit_date > span > i.anticon.anticon-calendar.ant-calendar-picker-icon > svg')
t1.click()

t2 = driver.find_element_by_css_selector(
    '#register_date > span > i.anticon.anticon-calendar.ant-calendar-picker-icon > svg > path')
t2.click()

t3 = driver.find_element_by_css_selector(
    '#become_vip_date > span > i.anticon.anticon-calendar.ant-calendar-picker-icon > svg')

t3.click()

search = driver.find_element_by_css_selector(
    '#manager_list_wrap > div.manager_list_search___2yZy_ > div > form > div.btn_group > button.ant-btn.btn_group_search.ant-btn-primary > div')
search.click()

driver.quit()

# ul_tag = driver.find_element_by_id('zyg_supercard_manage$Menu')
# li_tags = ul_tag.find_elements_by_class_name('li')
# print(li_tags[0])

# 注意这里必须要等待时间，因为代码运行过快，代码运行完的时候页面还没加载出来就会找不到元素

# time.sleep(2)
#
# ret = driver.find_element_by_id('1')
# ret2 = driver.find_element_by_id('2')
# print(ret.text)
# print('----------------------------------')
# print(ret2.text)
# # 是不是已宋曲开头
# if ret.text.startswith('宋曲'):
#     print('测试通过')
# else:
#     print('不通过')
# # 最后，driver.quit()让浏览器和驱动进程一起退出，不然桌面会有好多窗口
# driver.quit()
