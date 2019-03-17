# coding=utf-8
import ddt
import unittest
@ddt.ddt
class DataTestDdt(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        print('类开始')

    def setUp(self):
        print('测试开始')
    @classmethod
    def tearDownClass(self):
        print('类结束')
    def tearDown(self):
        print('测试结束')

    @ddt.data(
        [1,2],[3,4],[5,6],[7,8]
    )

    @ddt.unpack
    def testCase01(self,a,b):
        print(a+b)

if __name__ == "__main__":
    unittest.main()
