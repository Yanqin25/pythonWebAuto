# coding=utf-8

import unittest


class TestDemo2(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('类222执行前')

    @classmethod
    def tearDownClass(cls):
        print('类222执行后')

    def setUp(self):
        print("test222 start")

    def testcase02(self):
        print("test02 case")

    def testcase03(self):
        print("test03 case")

    @unittest.skip("不执行本条用例")
    def testcase01(self):
        print("test01 case")

    def tearDown(self):
        print("test222 end")


if __name__ == "__main__":
    unittest.main()  # 执行所有test开始的方法，执行顺序和方法名字顺序一致

    # 执行指定case，执行顺序和添加case顺序一致
    # suite=unittest.TestSuite()
    # suite.addTest(TestDemo('testcase1'))
    # suite.addTest(TestDemo('testcase2'))

    # unittest.TextTestRunner().run(suite)
