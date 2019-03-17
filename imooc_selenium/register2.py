# coding=utf-8
import sys
sys.path.append("E:/coding/yangqin/pythonAuto")
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
from ShowapiRequest import ShowapiRequest
import time
import string
import random
from find_element import FindElement


class RegisterFunction(object):

    def __init__(self, url):
        self.driver = self.get_driver(url)

    # 获取driver并打开url
    def get_driver(self, url):
        driver = webdriver.Chrome()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 获取注册页面元素
    def get_user_element(self, key):
        findElement = FindElement(self.driver)
        return findElement.get_element(key)

    # 获取随机用户
    def get_random_user(self, num):
        return ''.join(random.sample(string.ascii_letters+string.digits, num))

    # 保存验证码截图
    def get_code_image(self, fileName):
        self.driver.save_screenshot(fileName)
        code_el = self.get_user_element("code_img")
        left = code_el.location['x']
        top = code_el.location['y']
        right = left+code_el.size['width']
        bottom = top+code_el.size['height']
        image = Image.open(fileName).crop((left, top, right, bottom))
        image.save(fileName)

    # 获取验证码文本
    def get_code_text(self, file_name):
        self.get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4",
                           "62626", "d61950be50dc4dbd9969f741b8e730f5")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "1")
        r.addBodyPara("needMorePrecise", "1")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        return res.json()['showapi_res_body']['Result']  # 返回信息

    def main(self):
        username = self.get_random_user(5)
        userEmail = username+"@163.com"
        file_name = "./screenshot/code.png"
        code = self.get_code_text(file_name)
        self.send_user_info("user_email", userEmail)
        self.send_user_info("user_name", username)
        self.send_user_info("password", "111111")
        self.send_user_info("code_text", code)
        self.get_user_element("register_btn").click()
        code_err=self.get_user_element("code_text_err")
        self.driver.save_screenshot("./screenshot/codeerr.png") if code_err else print("code pass") 
        time.sleep(10)
        self.driver.close()


if __name__ == "__main__":
    register = RegisterFunction("http://www.5itest.cn/register")
    register.main()
