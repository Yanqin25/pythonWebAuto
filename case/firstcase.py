# coding=utf-8

import sys
sys.path.append("E:/coding/yangqin/pythonAuto")
import os
import time
import unittest
from util.HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from business.register_business import RegisterBusiness



class FirstCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.file_name=r"E:\coding\yangqin\pythonAuto\screenCapture\code.png"
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.driver.maximize_window()
        self.register_b = RegisterBusiness(self.driver)

    def tearDown(self):
        for method_name,error in self._outcome.errors:
            if error:
                # case_name=self._testMethodName
                case_name=str(method_name)[:str(method_name).find("(")]
                file_path=os.path.join(os.getcwd(),'screenCapture',case_name+'.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()

    def test_register_email_err(self):
        result = self.register_b.register_email_err(
            '7404@@qq.com', 'test1', '111111', self.file_name)
        # print('email校验失败！') if result else print("测试通过")
        self.assertFalse(result, "邮箱格式校验有误")

    def test_register_username_err(self):
        result = self.register_b.register_username_err(
            '74079865@qq.com', 't', '111111', self.file_name)
        # print('用户名校验失败！') if result else print("测试通过")
        self.assertFalse(result, "用户名校验有误")

    def test_register_password_err(self):
        result = self.register_b.register_password_err(
            'zhangshan@qq.com', 'zhanshan', '1', self.file_name)
        # print('密码校验失败！') if result else print("测试通过")
        self.assertFalse(result, "密码校验有误")

    def test_register_code_err(self):
        result = self.register_b.register_code_err(
            'zhangshan2@qq.com', 'zhanshan2', '111111', '2222')
        print('验证码校验失败！') if result else print("测试通过")

    def test_register_success(self):
        self.register_b.user_base(
            'yangqin@qq.com', 'yangqin', 'smile11', self.file_name)
        result = self.register_b.is_regester_success()
        # print('测试通过') if result else print("全部输入正确信息却注册失败")
        self.assertTrue(result, "有效等价类注册失败")
        
if __name__ == "__main__":
    # unittest.main()
    report_path = os.path.join(os.getcwd(), 'report', 'firstReport.html')
    with open(report_path, 'wb') as f:
        suite = unittest.TestSuite()
        suite.addTest(FirstCase("test_register_email_err"))
        suite.addTest(FirstCase("test_register_username_err"))
        suite.addTest(FirstCase("test_register_password_err"))
        suite.addTest(FirstCase("test_register_code_err"))
        suite.addTest(FirstCase("test_register_success"))
        runner = HTMLTestRunner(
            stream=f, title="this is first report", description=u"这是第一个测试报告", verbosity=2)
        runner.run(suite)
