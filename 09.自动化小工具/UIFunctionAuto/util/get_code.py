# coding=utf-8
from base.base import Base
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import os
from config import globalConfig
import pytesseract


class GetCode(object):
    def __init__(self, driver, configpath, node):
        self.__driver = driver
        self.__configpath = configpath
        self.__node = node
        self.__screenPath = globalConfig.CODE_IMG_SCREEN_PATH

    def __get_code_image(self, code_image_el):
        self.__driver.save_screenshot(self.__screenPath)
        code_el = Base(self.__driver,self.__configpath,self.__node).find_element(code_image_el)
        left = code_el.location['x']
        top = code_el.location['y']
        right = left+code_el.size['width']
        bottom = top+code_el.size['height']
        image = Image.open(self.__screenPath).crop((left, top, right, bottom))
        image.save(self.__screenPath)

    # 获取验证码文本通过第三方api，付费精度较高
    def get_code_text_api(self, code_image_el):
        self.__get_code_image(code_image_el)
        r = ShowapiRequest("http://route.showapi.com/184-4",
                           "62626", "d61950be50dc4dbd9969f741b8e730f5")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", self.__screenPath)  # 文件上传时设置
        res = r.post()
        return res.json()['showapi_res_body']['Result']  # 返回信息

    def get_code_text(self, code_img_el):
        self.__get_code_image(code_img_el)
        img = Image.open(self.__screenPath)
        text = pytesseract.image_to_string(img)
        return text
