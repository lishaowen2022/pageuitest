# author:lihua
# Time:2022/11/1 2:04 PM
import logging
from time import sleep

import pytest

from base.base_util import BaseUtil
from pageobject.login_page import LoginPage
from pageobject.wallet_page import WalletPage


class TestWalletPage(BaseUtil):
    #wallet page
    def test_wallet(self):

        # 调用登录方法
        lp = LoginPage(self.driver)
        lp.login_page_use_mobile(phone='812312312311', code='0000')
        sp=WalletPage(self.driver)
        sp.wallet_page(amount=100000)
