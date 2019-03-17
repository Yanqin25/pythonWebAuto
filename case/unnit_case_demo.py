# coding=utf-8

import unittest


class TestDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('类执行前')

    @classmethod
    def tearDownClass(cls):
        print('类执行后')

    def setUp(self):
        print("test start")

    def testcase2(self):
        print("test2 case")

    def testcase3(self):
        print("test3 case")

    @unittest.skip("不执行本条用例")
    def testcase1(self):
        print("test1 case")

    def tearDown(self):
        print("test end")


if __name__ == "__main__":
    unittest.main()  # 执行所有test开始的方法，执行顺序和方法名字顺序一致

    # 执行指定case，执行顺序和添加case顺序一致
    # suite=unittest.TestSuite()
    # suite.addTest(TestDemo('testcase1'))
    # suite.addTest(TestDemo('testcase2'))

    # unittest.TextTestRunner().run(suite)
