# coding=utf-8

from handle.register_handle import RegisterHandle


class RegisterBusiness(object):
    def __init__(self, driver):
        self.register_h = RegisterHandle(driver)

    def user_base(self, email, username, password, file_name):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(username)
        self.register_h.send_user_password(password)
        self.register_h.send_code(file_name)
        self.register_h.click_register_btn()


    def is_regester_success(self):
        return self.register_h.get_registerBtn_text() == None

    def register_function(self, email, username, password, code,assertCode):
        self.user_base(email, username, password, code)
        return self.register_h.get_err_text(assertCode)


    def register_email_err(self, email, username, password, file_name):
        self.user_base(email, username, password, file_name)
        return self.register_h.get_err_text("user_email_err") == None

    def register_username_err(self, email, username, password, file_name):
        self.user_base(email, username, password, file_name)
        return self.register_h.get_err_text("username_err") == None

    def register_password_err(self, email, username, password, file_name):
        self.user_base(email, username, password, file_name)
        return self.register_h.get_err_text("password_err") == None

    def register_code_err(self, email, username, password, file_name):
        self.user_base(email, username, password, file_name)
        return self.register_h.get_err_text("code_text_err") == None
