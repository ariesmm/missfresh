import unittest

from page.home_page import HomePage
from testcase.base_testcase import BaseTestCase


class HomeTestCase(BaseTestCase):
    def testhome(self):
        h=HomePage(self.driver)
        h.homepage('面包')




if __name__ == '__main__':
    unittest.main()