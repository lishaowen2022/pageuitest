# author:lihua
# Time:2022/11/1 2:02 PM
from time import sleep

import data
from base.base_page import BasePage
from base.base_util import BaseUtil
from common.global_parameter import login_code
from pageobject.analytics_page import AnalyticsPage
from pageobject.login_page import LoginPage


class TestAnalyticsPage(BaseUtil):
    #analytics page
    def test_analytics(self):

            # 调用登录方法
            lp = LoginPage(self.driver)
            lp.login_page_use_mobile(phone='822222223333333', code=login_code)
            ap=AnalyticsPage(self.driver)
            ap.analytics_page()

