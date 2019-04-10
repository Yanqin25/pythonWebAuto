# coding=utf-8
import os
import sys
sys.path.append(os.getcwd())
from util.HTMLTestRunner import HTMLTestRunner
from base.browser_engine import BrowserEngine
from page.memberMangement.login_page import LoginPage
import unittest
import time
class MechaincsCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserEngine().init_driver()

    def setUp(self):
        # self.driver.get("http://1807020009.pre-pool1-site.make.yun300.cn/blank7.html")
        self.driver.get("http://1809200008.test-pool1-site.make.yun300.cn/Signin.html")
        # self.driver.get("http://1809200008.test-pool1-site.make.yun300.cn")
        self.driver.maximize_window()
        self.login_p = LoginPage(self.driver)

    def tearDown(self):
        for method_name, error in self._outcome.errors:
            if error:
                # case_name=self._testMethodName
                case_name = str(method_name)[:str(method_name).find("(")]
                file_path = os.path.join(
                    os.getcwd(), 'screenShot', case_name+'.png')
                self.driver.save_screenshot(file_path)
    @classmethod
    def tearDownClass(cls):
        time.sleep(10)
        cls.driver.quit()

    # @ddt.data(*data)
    # def test_register_case(self, data):
    #     email, username, password, code, assertCode, assertText = data[1:]
    #     print(data[1:])
    #     result = self.register_b.register_function(
    #         email, username, password, code, assertCode)
    #     self.assertEqual(result, assertText, "测试失败")
    def test_login(self):
        self.login_p.login("13699495394","smile.11")



if __name__ == "__main__":
    unittest.main()
    # report_path = os.path.join(os.getcwd(), 'report', 'report.html')
    # with open(report_path, 'wb') as f:
    #     suite = unittest.TestLoader().loadTestsFromTestCase(MechaincsCase)
    #     runner = HTMLTestRunner(
    #         stream=f, title="this is first ddt report", description=u"这是第一个ddt测试报告", verbosity=2)
    #     runner.run(suite)
