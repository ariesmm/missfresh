
import unittest

from page.shopping_trolley_page import ShoppingTrolleyPage
from testcase.base_testcase import BaseTestCase


class Shopping_Cart(BaseTestCase):

    def test_Complete_shopping_cart(self):
        #登录购物车模块内一系类操作
        sp = ShoppingTrolleyPage(self.driver)
        sp.add_goods()
        sp.change_the_goods()
        sp.remove_goods()


if __name__ == '__main__':
    unittest.main()
