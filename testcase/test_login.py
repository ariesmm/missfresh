import unittest

from testcase.base_testcase import BaseTestCase
from page.login_page import LoginPage


class LoginTestCase(BaseTestCase):
    '''微信登录'''

    def test_login(self):
        lg = LoginPage(self.driver)
        result = lg.login()

        self.assertEqual("退出登录", result)


if __name__ == '__main__':
    unittest.main()
