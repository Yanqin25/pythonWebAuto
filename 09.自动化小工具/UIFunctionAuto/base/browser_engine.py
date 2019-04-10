from selenium import webdriver
from config import globalConfig


class BrowserEngine:

    def init_driver(self):
        option = webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        driver = webdriver.Chrome(options=option)
        # driver.find_element_by_xpath
        # driver.execute_script
        return driver
