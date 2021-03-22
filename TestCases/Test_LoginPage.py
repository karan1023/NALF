from Locators.LoginPage import LoginPageElements
import pytest

from TestCases.test_base import BaseTest


class TestLogin(BaseTest):

    @pytest.mark.skip
    def test_login01(self):
        self.loginpage = LoginPageElements(self.driver)
        self.loginpage.do_login('admin', 'admin@123')
        assert self.loginpage.do_gettitle() == 'UB :: Carmudi'

    def test_login02(self):
        self.loginpage = LoginPageElements(self.driver)

