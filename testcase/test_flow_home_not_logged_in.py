import unittest

from page.home_page import HomePage
from page.shopping_page import ShoppingPage
from page.shopping_trolley_page import ShoppingTrolleyPage
from testcase.base_testcase import BaseTestCase


class HomeTestCase(BaseTestCase):
    def testhome(self):
        '''首页搜索并加入购物车'''
        h=HomePage(self.driver)#实例化
        cart_result=h.homepage('面包')#搜索框传参
        s=ShoppingTrolleyPage(self.driver)
        s.ele_close_an_account()#调用结算
        p=ShoppingPage(self.driver)
        p.ele_pay()#调用支付
        balance_result=p.ele_balance_result()#结果验证
        self.assertIn('订单填写', balance_result)  # 断言



if __name__ == '__main__':
    unittest.main()