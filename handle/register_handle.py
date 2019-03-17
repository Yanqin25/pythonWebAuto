from page.register_page import RegisterPage
from util.get_code import GetCode

class RegisterHandle(object):
    def __init__(self,driver):
        self.driver=driver
        self.register_p=RegisterPage(driver)
    
    
    # 输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)

    # 输入用户名
    def send_user_name(self,username):
        self.register_p.get_username_element().send_keys(username)
    
    # 输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)
    
    # 输入验证码
    def send_code(self,file_name):
        try:
            code=GetCode(self.driver).get_code_text(file_name)
            self.register_p.get_code_element().send_keys(code) 
        except:
            self.register_p.get_code_element().send_keys(file_name) 
    

    # 获取错误提示信息
    def get_err_text(self,key):
        try:
            if key=="user_email_err":
                return self.register_p.get_email_err_element().text
            elif key=="username_err":
                return self.register_p.get_username_err_element().text
            elif key=="password_err":
                return self.register_p.get_password_err_element().text
            elif key=="code_text_err":
                return self.register_p.get_code_err_element().text
            else:
                return None
        except:
            return None


    # 点击注册按钮
    def click_register_btn(self):
        self.register_p.get_registerBtn_element().click()

    # 获取注册按钮文字
    def get_registerBtn_text(self):
        btn=self.register_p.get_registerBtn_element()
        return btn.text if btn else None
