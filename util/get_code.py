# coding=utf-8
from base.find_element import FindElement
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
class GetCode(object):
    def __init__(self,driver):
        self.driver=driver
    def __get_code_image(self, fileName):
        self.driver.save_screenshot(fileName)
        code_el = FindElement(self.driver).get_element("code_img")
        left = code_el.location['x']
        top = code_el.location['y']
        right = left+code_el.size['width']
        bottom = top+code_el.size['height']
        image = Image.open(fileName).crop((left, top, right, bottom))
        image.save(fileName)

    # 获取验证码文本
    def get_code_text(self, file_name):
        self.__get_code_image(file_name)
        r = ShowapiRequest("http://route.showapi.com/184-4",
                           "62626", "d61950be50dc4dbd9969f741b8e730f5")
        r.addBodyPara("typeId", "35")
        r.addBodyPara("convert_to_jpg", "0")
        r.addBodyPara("needMorePrecise", "0")
        r.addFilePara("image", file_name)  # 文件上传时设置
        res = r.post()
        return res.json()['showapi_res_body']['Result']  # 返回信息
