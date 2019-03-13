#coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

driver=webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(2)
title=EC.title_contains("注册") # 判断页面title是否正确
# print(title(driver))
if title(driver):
    driver.find_element_by_id("register_email").send_keys('740479865@qq.com')
    driver.find_element_by_name("nickname").send_keys('mufeng')
    driver.find_element_by_name("password").send_keys('123456')
    driver.find_element_by_name("captcha_code").send_keys('123455')
# 给一个定位方式，判断是否存在
locator=(By.ID,"register_email2")
exist=WebDriverWait(driver,1).until(EC.visibility_of_element_located(locator))
print(exist)
driver.close()