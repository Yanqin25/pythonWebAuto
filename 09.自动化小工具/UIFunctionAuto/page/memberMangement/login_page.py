from base.base import Base
from util.get_code import GetCode
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import os
import time


class LoginPage(Base):
    def __init__(self, driver, configPath=os.path.join(os.getcwd(),"config/memberMangement.ini"), node='login'):
        self.__dirver = driver
        super().__init__(driver, configPath, node)

    def login(self, username, password, code=None):
        self.send_keys(self.find_element("username"), username)
        self.send_keys(self.find_element("password"), password)
        if code==None:
            self.__send_code_auto(3)
            # code=GetCode(self.__dirver, os.path.join(
            #     os.getcwd(), "config/memberMangement.ini"), "login").get_code_text_api("code_img")
            # self.send_keys(self.find_element("code"), code)
            # self.find_element("loginBtn").click()
        else:
            self.send_keys(self.find_element("code"), code)
            self.find_element("loginBtn").click()

        # self.send_keys(self.find_element("code"), code)
        # self.find_element("loginBtn").click()

    
    def __send_code_auto(self,n):
        '''自动获取验证码，当验证码错误时，重试n次
        '''
        code_err_num=0
        getCode=GetCode(self.__dirver, os.path.join(
            os.getcwd(), "config/memberMangement.ini"), "login")
        while code_err_num<n:
            if(code_err_num!=0):
                self.find_element("change_code").click()
            time.sleep(1)
            code=getCode.get_code_text("code_img")
            self.send_keys(self.find_element("code"), code)
            self.find_element("loginBtn").click()
            break
            # if  self.code_valid_err():
            #     code_err_num+=1
            #     continue
            # else:
            #     break


    def code_valid_err(self):
        try:
            code_err=self.find_element("valid_code_err_text",0.5)            
            # return code_err.text==business_const.LOGIN_VALID_CODE_ERR
            return True if code_err else False
        except:
            return False
        
