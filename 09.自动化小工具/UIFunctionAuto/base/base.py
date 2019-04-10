from config import globalConfig
from util.read_config import ReadConfig
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By


class Base():
    def __init__(self, driver, configpath, node):
        self.__driver = driver
        self.__configpath = configpath
        self.__node = node
        self.readConfig = ReadConfig(self.__configpath, self.__node)

    def find_element(self, key, timeout=None):
        try:
            by, value = self.readConfig.get_element_value(key).split(":", 1)
            if by == 'id':
                return self.__init_wait(timeout).until(EC.visibility_of_element_located((By.ID, value)))
            elif by == 'name':
                return self.__init_wait(timeout).until(EC.visibility_of_element_located((By.NAME, value)))
            elif by == 'classname':
                return self.__init_wait(timeout).until(EC.visibility_of_element_located((By.CLASS_NAME, value)))
            elif by == 'tag':
                return self.__init_wait(timeout).until(EC.visibility_of_element_located((By.TAG_NAME, value)))
            elif by == 'link':
                return self.__init_wait(timeout).until(EC.visibility_of_element_located((By.LINK_TEXT, value)))
            elif by == 'partialLink':
                return self.__init_wait(timeout).until(EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, value)))
            elif by == 'css':
                return self.__init_wait(timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, value)))
            elif by == 'xpath':
                return self.__init_wait(timeout).until(EC.visibility_of_element_located((By.XPATH, value)))
            else:
                print("by值错误:{}".format(by))
                self.__driver.quit()
        except (NoSuchElementException, TimeoutException):
            self.__driver.quit()
            raise TimeoutException(
                msg='定位元素失败, 定位方式为: {}-->{}'.format(by, value))

    def find_elements(self, key, timeout=None):

        try:
            by, value = self.readConfig.get_element_value(key).split(":", 1)
            if by == 'id':
                return self.__init_wait(timeout).until(EC.visibility_of_all_elements_located((By.ID, value)))
            elif by == 'name':
                return self.__init_wait(timeout).until(EC.visibility_of_all_elements_located((By.NAME, value)))
            elif by == 'classname':
                return self.__init_wait(timeout).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, value)))
            elif by == 'tag':
                return self.__init_wait(timeout).until(EC.visibility_of_all_elements_located((By.TAG_NAME, value)))
            elif by == 'link':
                return self.__init_wait(timeout).until(EC.visibility_of_all_elements_located((By.LINK_TEXT, value)))
            elif by == 'partialLink':
                return self.__init_wait(timeout).until(EC.visibility_of_all_elements_located((By.PARTIAL_LINK_TEXT, value)))
            elif by == 'css':
                return self.__init_wait(timeout).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, value)))
            elif by == 'xpath':
                return self.__init_wait(timeout).until(EC.visibility_of_all_elements_located((By.XPATH, value)))
                # return self.__driver.find_elements_by_xpath(value)
            else:
                print("by值错误:{}".format(by))
                self.__driver.quit()
        except (NoSuchElementException, TimeoutException):
            self.__driver.quit()
            raise TimeoutException(
                msg='定位元素失败, 定位方式为: {}-->{}'.format(by, value))

    def send_keys(self, webElement, value):
        webElement.clear()
        webElement.send_keys(value)

    def find_subElements_by_calssname(self, element, classname):
        try:
            result = element.find_elements_by_class_name(classname)
            return result
        except:
            return None

    def find_subElements_by_tag_name(self, element, tagName):
        try:
            result = element.find_elements_by_tag_name(tagName)
            return result
        except:
            return None

    def __init_wait(self, timeout):
        if timeout is None:
            return WebDriverWait(driver=self.__driver, timeout=globalConfig.UI_WAIT_TIME)
        else:
            return WebDriverWait(driver=self.__driver, timeout=timeout)

    def contain_classname(self, webElement, classname):
        return classname in webElement.get_attribure('class')

    def wait_until_el_invisibility(self, webElement, timeout=None):
        return self.__init_wait(timeout).until(EC.invisibility_of_element(webElement))

    def wait_element_selected(self, webElement, timeout=None):
        return self.__init_wait(timeout).until(EC.element_to_be_selected(webElement))

    def element_is_checked(self, webElement):
        return webElement.is_selected()

    def element_to_be_clickable(self, key, timeout=None):
        try:
            by, value = self.readConfig.get_element_value(key).split(":", 1)
            if by == 'id':
                return self.__init_wait(timeout).until(EC.element_to_be_clickable((By.ID, value)))
            elif by == 'name':
                return self.__init_wait(timeout).until(EC.element_to_be_clickable((By.NAME, value)))
            elif by == 'classname':
                return self.__init_wait(timeout).until(EC.element_to_be_clickable((By.CLASS_NAME, value)))
            elif by == 'tag':
                return self.__init_wait(timeout).until(EC.element_to_be_clickable((By.TAG_NAME, value)))
            elif by == 'link':
                return self.__init_wait(timeout).until(EC.element_to_be_clickable((By.LINK_TEXT, value)))
            elif by == 'partialLink':
                return self.__init_wait(timeout).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, value)))
            elif by == 'css':
                return self.__init_wait(timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, value)))
            elif by == 'xpath':
                return self.__init_wait(timeout).until(EC.element_to_be_clickable((By.XPATH, value)))
            else:
                print("by值错误:{}".format(by))
                self.__driver.quit()
        except (NoSuchElementException, TimeoutException):
            self.__driver.quit()
            raise TimeoutException(
                msg='定位元素失败, 定位方式为: {}-->{}'.format(by, value))
