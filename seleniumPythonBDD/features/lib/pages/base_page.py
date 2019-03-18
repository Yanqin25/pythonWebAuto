
from util.read_ini import ReadIni


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def get_title(self):
        return self.driver.title

    def find_element(self, key):
        read_ini = ReadIni()
        data = read_ini.get_value(key)
        by, value = data.split(':', 1)
        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None
