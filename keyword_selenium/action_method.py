# coding=utf-8
from selenium import webdriver
from base.location_ele import LocationElement
import time


class ActionMethod():

    # 打开浏览器
    def open_browser(self, browser):
        if browser == 'chrome':
            self.driver = webdriver.Chrome()
        elif browser == 'firefox':
            self.driver = webdriver.Firefox()
        else:
            self.driver = webdriver.Edge()

    # 输入地址
    def get_url(self, url):
        self.driver.get(url)

    # 定位元素
    def find_element(self, location):
        return LocationElement(self.driver).get_element(location)

    # 输入元素
    def element_send_val(self, val, location):
        element = self.find_element(location)
        element.send_keys(val)

    # 点击元素
    def element_click(self, location):
        self.find_element(location).click()

    # 等待
    def wait(self, times=2):
        time.sleep(times)

    # 关闭浏览器
    def close_browser(self):
        self.driver.close()

    # 获取title
    def get_title(self):
        return self.driver.title
