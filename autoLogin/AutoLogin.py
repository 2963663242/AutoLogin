import time
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pickle
#先安装pywin32，才能导入下面两个包
import win32api
import win32con
#导入处理alert所需要的包
from selenium.common.exceptions import NoAlertPresentException
import traceback
import json

if __name__ == '__main__':
    #环境配置
    chromedriver = "C:\Program Files (x86)\Google\Chrome\Application"
    os.environ["webdriver.ie.driver"] = chromedriver
    capa = DesiredCapabilities.CHROME
    capa["pageLoadStrategy"] = "none"
    #option = webdriver.ChromeOptions()
    #option.add_argument("--user-data-dir=" + r"C:\Users\Administrator\AppData\Local\Google Chrome\ChromeUserData")
    driver = webdriver.Chrome(desired_capabilities=capa)

    driver.get('https://www.instagram.com/') # 打开网站
    driver.maximize_window() #最大化谷歌浏览器
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "username")))
    #处理alert弹窗
    try:
        alert1 = driver.switch_to.alert #switch_to.alert点击确认alert
    except NoAlertPresentException as e:
        print("no alert")
        traceback.print_exc()
    else:
        at_text1 = alert1.text
        print("at_text:" + at_text1)

   # time.sleep(3)



    username = "8618879355958" # 请替换成你的用户名
    password = "a13576301231" # 请替换成你的密码

    driver.find_element_by_name('username').click() # 点击用户名输入框
    driver.find_element_by_name('username').clear() #清空输入框
    driver.find_element_by_name('username').send_keys(username) # 自动敲入用户名

    driver.find_element_by_name('password').click() # 点击密码输入框
    driver.find_element_by_name('password').clear() #清空输入框
    driver.find_element_by_name('password').send_keys(password) # 自动敲入密码

    #采用class定位登陆按钮
    #driver.find_element_by_class_name('sqdOP  L3NKy   y3zKF     ').click() # 点击“登录”按钮
    #采用xpath定位登陆按钮，
    #driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
    driver.find_element_by_css_selector('button[type="submit"]').click() # 点击“账户登录”
    element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='button']")))
    time.sleep(3)
    #driver.find_element_by_id('signIn').click() # 点击“签到”

    win32api.keybd_event(122,0,0,0)  #F11的键位码是122，按F11浏览器全屏
    win32api.keybd_event(122,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
    cookie = driver.get_cookies()  # 获取cookie
    pickle.dump(cookie, open('taobao_cookies.txt', 'wb'))
    print(cookie)
    driver.close()

    # 代码调用：
    # python.exe JDSignup.py
    # 可以将这行命令添加到Windows计划任务，每天运行，从而实现每日自动签到领取京豆。
