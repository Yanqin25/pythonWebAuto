# coding=utf-8
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
from ShowapiRequest import ShowapiRequest
import time
import string
import random

driver = webdriver.Chrome()
driver.get("http://www.5itest.cn/register")
time.sleep(2)
title = EC.title_contains("注册")  # 判断页面title是否正确
# print(title(driver))
email_el = driver.find_element_by_id("register_email")
print(email_el.get_attribute("placeholder"))
email = ''.join(random.sample(
    string.ascii_letters+string.digits, 5))+'@qq.com'
email_el.send_keys(email)
print(email_el.get_attribute("value"))
driver.find_element_by_name("nickname").send_keys('mufeng')
driver.find_element_by_name("password").send_keys('123456')
# 给一个定位方式，判断是否存在
locator = (By.ID, "register_email")
exist = WebDriverWait(driver, 1).until(
    EC.visibility_of_element_located(locator))
print(exist)

# 截屏获取验证码
driver.save_screenshot('./screenshot/code.png')
code_el = driver.find_element_by_id('getcode_num')
left = code_el.location['x']
top = code_el.location['y']
right = left+code_el.size['width']
bottom = top+code_el.size['height']

im = Image.open('./screenshot/code.png')
img = im.crop((left, top, right, bottom))
img.save('./screenshot/code1.png')

# 解析验证码
r = ShowapiRequest("http://route.showapi.com/184-4",
                   "89459", "eaa40d8760814950b8f216c9f0a4c5c2")
r.addBodyPara("typeId", "35")
r.addBodyPara("convert_to_jpg", "1")
r.addBodyPara("needMorePrecise", "1")
r.addFilePara("image", r"./screenshot/code1.png")  # 文件上传时设置
res = r.post()
text = res.json()['showapi_res_body']['Result']  # 返回信息
time.sleep(2)
driver.find_element_by_name("captcha_code").send_keys(text)
time.sleep(5)
driver.close()
