import unittest

from driver.app_driver import appdriver

'''基本用例层'''
class BaseTestCase(unittest.TestCase):
    def setUp(self):
        self.driver=appdriver() #调用原始驱动

    def tearDown(self):
        self.driver.quit() #退出




if __name__ == '__main__':
    unittest.main()
