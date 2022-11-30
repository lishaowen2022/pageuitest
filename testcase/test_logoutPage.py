# author:lihua
# Time:2022/11/1 4:59 PM
from time import sleep

from base.base_util import BaseUtil
from common.global_parameter import img_url
from pageobject.login_page import LoginPage
from pageobject.logout_page import LogoutPage


class TestLogoutPage(BaseUtil):
    #logout
    def test_logout(self):
        lp = LoginPage(self.driver)
        lp.login_page_use_mobile(phone='8123123123', code='0000')
        sp=LogoutPage(self.driver)
        sp.logout_page()