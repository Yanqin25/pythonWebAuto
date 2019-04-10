# coding=utf-8
import os
from base.base import Base


class ShopcartPage(Base):
    def __init__(self, driver, configPath=os.path.join(os.getcwd(), "config/mechaincsOrder.ini"), node='shopcart'):
        self.__dirver = driver
        super().__init__(driver, configPath, node)

    def select_product(self, indexList):
        for index in indexList:
            el=self.find_elements("product_checkbox")[index-1]
            flag=self.element_is_checked(el)
            if not flag:
                el.click()

    def get_shopcart_num(self):
        return len(self.find_elements("product_checkbox"))

    def to_settlement(self):
        return self.find_element("settlement").click()
