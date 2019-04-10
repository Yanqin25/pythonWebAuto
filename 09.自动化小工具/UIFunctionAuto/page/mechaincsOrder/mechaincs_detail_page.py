# coding=utf-8
from base.base import Base
import os
import re
import time

class MechaincsDetailPage(Base):
    def __init__(self, driver, configPath=os.path.join(os.getcwd(), "config/mechaincsOrder.ini"), node='mechaincsDetail'):
        self.__driver = driver
        super().__init__(driver, configPath, node)

    def add_shopcart(self, specList, num=None):
        if num == None:
            num = self.get_num()
        self.select_num(num)
        for spec in specList:
            self.select_spec(spec)
            self.find_element("add_shopcart").click()
            if not self.is_add_cart_sccuess():
                break
            time.sleep(3)
    def is_add_cart_sccuess(self):
        try:
            el=self.find_element("add_shopcart_success_tips")
            return True if el else False
        except:
            return False
        

    def to_buy(self, spec, num=None):
        if num == None:
            num = self.get_num()
        self.select_num(num)
        self.select_spec(spec)
        self.find_element("to_buy").click()
    #"红>中"
    def select_spec(self, spec):
        specList=spec.split(">")
        specArea=self.find_elements("product_spec")
        for i in range(len(specList)):
            xpath=".//div[contains(@class,'p_Product ')]//div[contains(text(),'{}')]".format(specList[i])
            el=specArea[i].find_element_by_xpath(xpath)
            el.click()
            

    def select_num(self, num):
        self.send_keys(self.find_element("buy_num"), num)

    def get_spec(self):
        speclist=self.find_elements("product_spec")
        print(speclist)
        result = {}
        for spec in speclist:
            spec_key = spec.text
            spec_val_elList = self.find_subElements_by_calssname(spec,"p_Product")
            spec_val = []
            for el in spec_val_elList:
                img=self.find_subElements_by_tag_name(el,"img")
                if img!=None and len(img)!=0:
                    spec_val.append(img[0].get_attribute("title"))
                else:
                    spec_val=spec_key.split("\n")[1:]
                    spec_key=spec_key.split("\n")[0].split("：")[0].strip()
                    break
            result[spec_key] = spec_val
        return result
    
    def get_num(self):
        return self.find_element("buy_num").get_attribute("value")

    def get_detail_dict(self):
        result = {}
        # 适用机型
        try:
            vals = self.find_elements("apply_model")
            appliList = [el.text for el in vals]
            result[self.find_element("apply_key").text.split("：")[
                0].strip()] = appliList
        except:
            result["适用机型"]=None
        # 概要
        try:
            result[self.find_element("out_box_key").text.split(
                "：")[0].strip()] = self.find_element("out_box").text
        except:
            result["概要"]=None

        # 零售价，市场价
        try:
            salKey = self.find_element("sale_key").text
            salVal = self.find_element("sale_val").text
            salUnit = self.find_element("sale_unit").text
            result[salKey.split("：")[0].strip()] = salVal+salUnit
        except:
            result["零售价"]=None
        try:
            marketKey = self.find_element("market_key").text
            marketVal = self.find_element("market_val").text
            marketUnit = self.find_element("market_unit").text
            result[marketKey.split("：")[0].strip()] = marketVal+marketUnit            
        except:
            result["市场价"]=None

        # 库存
        try:
            key = self.find_element("stock_key").text
            val = self.find_element("stock_val").text
            valunit = self.find_element("stock_unit").text
            result[key.split("：")[0].strip()] = val+valunit
        except:
            result["库存"]=None

        infoElements = self.find_elements("detail_info")
        for element in infoElements:
            key = element.find_elements_by_class_name(
                'e_title')[0].text.split("：")[0].strip()
            # key=re.search("[\u4e00-\u9fa5\w]+",key).group().strip()
            val = element.find_elements_by_class_name('e_title')[-1].text
            result[key] = val
        return result
