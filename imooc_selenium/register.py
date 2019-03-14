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


def driver_init():
    driver.get("http://www.5itest.cn/register")
    driver.maximize_window()
    time.sleep(5)


def get_elementById(id):
    return driver.find_element_by_id(id)

# 产生随机数
def get_random(num):
    return ''.join(random.sample(string.ascii_letters+string.digits, num))


def get_code_image(file_name):
    driver.save_screenshot(file_name)
    code_el = get_elementById("getcode_num")
    left = code_el.location['x']
    top = code_el.location['y']
    right = left+code_el.size['width']
    bottom = top+code_el.size['height']
    image = Image.open(file_name).crop((left, top, right, bottom))
    image.save(file_name)


def get_code_text(file_name):
    r = ShowapiRequest("http://route.showapi.com/184-4",
                       "89459", "eaa40d8760814950b8f216c9f0a4c5c2")
    r.addBodyPara("typeId", "35")
    r.addBodyPara("convert_to_jpg", "1")
    r.addBodyPara("needMorePrecise", "1")
    r.addFilePara("image", file_name)  # 文件上传时设置
    res = r.post()
    return res.json()['showapi_res_body']['Result']  # 返回信息

# 运行主程序
def run_main():
    driver_init()
    username=get_random(6)
    userEmail=username+"@163.com"
    file_name='./screenshot/code.png'
    get_elementById("register_email").send_keys(userEmail)
    get_elementById("register_nickname").send_keys(username)
    get_elementById("register_password").send_keys("111111")
    get_code_image(file_name)
    code=get_code_text(file_name)
    get_elementById("captcha_code").send_keys(code)
    get_elementById("register-btn").click()
    time.sleep(5)
    driver.close()

run_main()