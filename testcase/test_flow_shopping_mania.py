
import unittest
from page.shopping_page import ShoppingPage
from testcase.base_testcase import BaseTestCase

class Shopping_Mania(BaseTestCase):

    def test_shopping_center(self):
        #登录购物流程
        lp = ShoppingPage(self.driver)
        lp.shopping_mania('面包')


if __name__ == '__main__':
    unittest.main()
