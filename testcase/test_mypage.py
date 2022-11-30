# author:lihua
# Time:2022/11/1 11:55 AM
import json
from time import sleep

import pytest
from selenium import webdriver
from base.base_add_cookie import BaseAddCookie
from base.base_util import BaseUtil

from pageobject.login_page import LoginPage
from pageobject.mypage import MyPage


class TestMyPage(BaseUtil):
    #my pages
    def test_mypage(self):

        # 调用登录方法
        lp = LoginPage(self.driver)
        lp.login_page_use_mobile(phone='877777777123', code='0000')
        mp=MyPage(self.driver)
        mp.my_page()
