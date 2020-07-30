
import unittest
from page.shopping_page import ShoppingPage
from testcase.base_testcase import BaseTestCase

class Shopping_Mania(BaseTestCase):

    def test_shopping_center(self):
        #登录购物流程
        lp = ShoppingPage(self.driver)
        lp.shopping_mania('面包')
        balance = lp.ele_balance_result()
        self.assertIn('订单填写',balance)
        print('进入订单支付页面')


if __name__ == '__main__':
    unittest.main()
