# coding=utf-8
import os
from base.base import Base
import time


class SettlementPage(Base):
    def __init__(self, driver, configPath=os.path.join(os.getcwd(),"config/mechaincsOrder.ini"), node='settlement'):
        self.__dirver = driver
        super().__init__(driver, configPath, node)

    def submit_order(self):
        self.find_element("address_select")
        self.find_element("submit_order").click()

    def back_shopCart_list(self):
        self.find_element("address_select")
        self.find_element("back_shopcart_list").click()


