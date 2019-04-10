# coding=utf-8
import os
import sys
sys.path.append(os.getcwd())
import time
import unittest
from config import globalConfig
from page.orderPayment.settlement_page import SettlementPage
from page.memberMangement.login_page import LoginPage
from page.orderPayment.shopcart_page import ShopcartPage
from page.orderPayment.shopcart_float_page import ShopcartFloatPage
from page.mechaincsOrder.mechaincs_detail_page import MechaincsDetailPage
from util.HTMLTestRunner import HTMLTestRunner
from base.browser_engine import BrowserEngine



class MechaincsDetailCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = BrowserEngine().init_driver()

    def setUp(self):
        # self.driver.get("http://1809200008.test-pool1-site.make.yun300.cn/productParts/47.html")
        self.driver.get("http://1807020009.pre-pool1-site.make.yun300.cn/productParts/72.html")
        self.driver.maximize_window()
        self.mechaincs_p = MechaincsDetailPage(self.driver)
        self.shortCartFloat_p = ShopcartFloatPage(self.driver)
        self.shortCart_p = ShopcartPage(self.driver)
        self.login_p = LoginPage(self.driver)
        self.settlement_p = SettlementPage(self.driver)

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
        # time.sleep(20)
        cls.driver.quit()

    @unittest.skip("暂不执行")
    def test_my(self):
        self.assertEqual(2, 3)
    # @unittest.skip("暂不执行")

    def test_shopcart_delete_after_shopping(self):
        '''被购买的商品应该从购物车删除'''
        self.driver.implicitly_wait(5)
        # self.mechaincs_p.add_shopcart(['红色>三居','蓝色>四居'])
        self.mechaincs_p.add_shopcart(['蓝>中','红>大'])
        self.shortCartFloat_p.to_settlement()
        time.sleep(0.5)
        self.shortCart_p.select_product([1,2])
        self.shortCart_p.to_settlement()

        time.sleep(0.5)
        self.login_p.login("13699495394", "smile.11")

        
        self.settlement_p.back_shopCart_list()
        beforNum = self.shortCart_p.get_shopcart_num()
        self.driver.back()

        self.settlement_p.submit_order()
        self.driver.back()
        self.settlement_p.back_shopCart_list()
        afterNum = self.shortCart_p.get_shopcart_num()

        print("将要购买商品数:{}，购买前购物车数量：{}，购买后购物车数量:{}".format(2,beforNum, afterNum))
        self.assertEqual(beforNum-afterNum, 2)

        


if __name__ == "__main__":
    # unittest.main()
    report_path = os.path.join(os.getcwd(), 'report', 'report.html')
    with open(report_path, 'wb') as f:
        suite = unittest.TestLoader().loadTestsFromTestCase(MechaincsDetailCase)
        runner = HTMLTestRunner(
            stream=f, title="Machine Order Repoter", description=u"机械订购测试报告", verbosity=2)
        runner.run(suite)
