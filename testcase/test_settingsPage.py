# author:lihua
# Time:2022/11/1 2:03 PM
from time import sleep

from base.base_util import BaseUtil
from common.global_parameter import ins_account,password
from pageobject.login_page import LoginPage
from pageobject.settings_page import SettingsPage


class TestSettingsPage(BaseUtil):
    #settings page
    def test_settings(self):
        # 调用登录方法
        lp = LoginPage(self.driver)
        lp.login_page_use_mobile(phone='820216100111111111111', code='0000')
        sp=SettingsPage(self.driver)
        sp.settings_page()