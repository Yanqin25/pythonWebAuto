# coding=utf-8
import os
from base.base import Base


class ShopcartFloatPage(Base):
    def __init__(self, driver, configPath=os.path.join(os.getcwd(),"config/mechaincsOrder.ini"), node='shopCartFloat'):
        self.__dirver = driver
        super().__init__(driver, configPath, node)

    def to_settlement(self):
        self.find_element("shopcartFloat_list").click()
        self.find_element("to_settlement").click()


