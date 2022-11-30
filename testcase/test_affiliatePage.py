# author:lihua
# Time:2022/11/10 4:42 PM
from base.base_util import BaseUtil
from common.global_parameter import product_name, affiliate_url, login_code
from pageobject.affiliate_page import AffiliatePage
from pageobject.login_page import LoginPage


class TestAffiliatePage(BaseUtil):
    #analytics page
    def test_affiliate(self):
        # 调用登录方法
        lp = LoginPage(self.driver)
        lp.login_page_use_mobile(phone='899990000', code=login_code)
        ap=AffiliatePage(self.driver)
        ap.affiliate_page(url=affiliate_url,product=product_name)

