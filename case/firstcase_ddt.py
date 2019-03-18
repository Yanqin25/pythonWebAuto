# coding=utf-8

import sys
sys.path.append("E:/coding/yangqin/pythonAuto")
import os
import time
import unittest
from util.HTMLTestRunner import HTMLTestRunner
from selenium import webdriver
from business.register_business import RegisterBusiness
from util.excel_util import ExcelUtil
import ddt
import unittest
data=ExcelUtil().get_data()
@ddt.ddt
class RegisterCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name=r"E:\coding\yangqin\pythonAuto\screenCapture\code.png"
    def setUp(self):
        print("用例开始执行")
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.driver.maximize_window()
        self.register_b = RegisterBusiness(self.driver)

    def tearDown(self):
        print("用例执行结束")
        for method_name,error in self._outcome.errors:
            if error:
                # case_name=self._testMethodName
                case_name=str(method_name)[:str(method_name).find("(")]
                file_path=os.path.join(os.getcwd(),'screenCapture',case_name+'.png')
                self.driver.save_screenshot(file_path)
        self.driver.close()

    # @ddt.data(
    #     ['12','Mushishi01','111111','code','user_email_err','请输入有效的电子邮件地址'],
    #     ['@qq.com','Mushishi01','111111','code','user_email_err','请输入有效的电子邮件地址'],
    #     ['12@qq.com','Mushishi01','111111','code','user_email_err','请输入有效的电子邮件地址']
    # )
    # @ddt.unpack
    @ddt.data(*data)
    def test_register_case(self,data):
        email,username,password,code,assertCode,assertText=data
        result = self.register_b.register_function(email,username,password,code,assertCode)
        self.assertEqual(result,assertText,"测试失败")


if __name__ == "__main__":
    # unittest.main()
    report_path = os.path.join(os.getcwd(), 'report', 'firstReportDdt.html')
    with open(report_path, 'wb') as f:
        suite = unittest.TestLoader().loadTestsFromTestCase(RegisterCase)
        runner = HTMLTestRunner(
            stream=f, title="this is first ddt report", description=u"这是第一个ddt测试报告", verbosity=2)
        runner.run(suite)
