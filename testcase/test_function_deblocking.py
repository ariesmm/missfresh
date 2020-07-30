import unittest

from page.deblocking_page import Deblocking


from testcase.base_testcase import BaseTestCase

'''解锁'''
class DeblockingTestCase(BaseTestCase):
    def test_deblocking(self):
        driver = self.driver
        all = [7, 4, 1, 5, 9, 6, 3]  # 键盘九宫格
        direction = 'up'

        deblicking=Deblocking(driver) # 实例化
        deblicking.deblocking(all,direction)  # 传入九宫格和驱动

if __name__ == '__main__':
    unittest.main()
