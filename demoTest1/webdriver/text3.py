# encoding=utf-8
# 上面这句话看起来是注释，但其实是有用的，指明了这个脚本的字符集编码格式
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def get_url():
    #
    url = 'https://login.taobao.com/'
    ch_options = webdriver.ChromeOptions()

    # 不加载图片,加快访问速度
    ch_options.add_experimental_option("prefs", {"profile.mamaged_default_content_settings.images": 2})

    # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
    ch_options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # ch_options.add_argument('--headless')  # 无头模式
    # ch_options.add_experimental_option("debuggerAddress", "127.0.0.1:9999")
    ch_options.add_argument('--proxy--server=127.0.0.1:8080')
    ch_options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
    ch_options.add_argument('--incognito')
    browser = webdriver.Chrome(options=ch_options)
    browser.maximize_window()
    wait = WebDriverWait(browser, 10)

    # 打开网页
    browser.get(url)

    # 等待 密码登录选项 出现
    password_login = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.qrcode-login > .login-links > .forget-pwd')))
    password_login.click()

    # 等待 微博登录选项 出现
    weibo_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.weibo-login')))
    weibo_login.click()

    # 获取账号输入框
    EMAIL = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(2) > div >input')))
    EMAIL.send_keys('微博账号')  # 填入微博账号

    # 获取密码输入框
    PASSWD = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(3) > div > input')))
    PASSWD.send_keys('微博密码')  # 填入微博密码

    time.sleep(2)

    # 获取登陆按钮
    button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, '#pl_login_logged > div > div:nth-child(7) > div:nth-child(1) > a > span')))
    button.click()
    cookies_list = browser.get_cookies()
    cookie_dict = {i["name"]: i["value"] for i in cookies_list}
    # print(cookie_dict)

    time.sleep(2)
    taobao_name = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,
                                                             '.site-nav-bd > ul.site-nav-bd-l > li#J_SiteNavLogin > div.site-nav-menu-hd > div.site-nav-user > a.site-nav-login-info-nick ')))
    # 输出淘宝昵称
    print(taobao_name.text)
    # 点击搜索
    browser.find_element_by_class_name('btn-search').click()
    cookies_list = browser.get_cookies()
    cookie_dict = {i["name"]: i["value"] for i in cookies_list}
    print(cookie_dict)
    browser.close()


get_url()
# 输出淘宝名称与进入淘宝所携带的cookies
# 可尝试通过淘宝cookies来爬取1688网的数据信息
