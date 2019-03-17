# coding=utf-8
from base.find_element import FindElement
class RegisterPage(object):
    def __init__(self,driver):
        self.fd=FindElement(driver)
    
    # 获取邮箱元素
    def get_email_element(self):
        return self.fd.get_element("user_email")
    
    # 获取用户名元素
    def get_username_element(self):
        return self.fd.get_element("username")

    # 获取密码元素
    def get_password_element(self):
        return self.fd.get_element("password")
    
    # 获取验证码元素
    def get_code_element(self):
        return self.fd.get_element("code_text")

    # 获取注册按钮元素
    def get_registerBtn_element(self):
        return self.fd.get_element("register_btn")

    # 获取邮箱错误元素
    def get_email_err_element(self):
        return self.fd.get_element("user_email_err")
    
    # 获取用户名错误元素
    def get_username_err_element(self):
        return self.fd.get_element("username_err")

    # 获取密码错误元素
    def get_password_err_element(self):
        return self.fd.get_element("password_err")

    # 获取验证码错误元素
    def get_code_err_element(self):
        return self.fd.get_element("code_text_err")
    
