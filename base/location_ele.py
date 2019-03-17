# encoding=utf-8


class LocationElement(object):
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, location):
        try:
            arr = location.split(':',1)
            by, value = arr[0], arr[1]
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'classname':
                return self.driver.find_element_by_class_name(value)
            else:
                return self.driver.find_element_by_xpath(value)
        except:
            return None
