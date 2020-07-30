import unittest

from page.home_page import HomePage
from testcase.base_testcase import BaseTestCase


class HomeTestCase(BaseTestCase):
    def testhome(self):
        h=HomePage(self.driver)
        cart_result=h.homepage('面包')
        self.assertIn('购物车',cart_result)


if __name__ == '__main__':
    unittest.main()