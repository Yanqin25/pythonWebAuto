
from seleniumPythonBDD.features.lib.pages.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, context):
        super(RegisterPage, self).__init__(context.driver)

    def send_email(self, email):
        self.find_element("user_email").send_keys(email)

    def send_username(self, username):
        self.find_element("username").send_keys(username)

    def send_password(self, password):
        self.find_element("password").send_keys(password)

    def send_code(self, code):
        self.find_element("code_text").send_keys(code)

    def click_register_btn(self):
        self.find_element("register_btn").click()

    def get_code_err_text(self):
        return self.find_element("code_text_err").text
