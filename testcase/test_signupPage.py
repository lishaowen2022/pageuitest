# author:lihua
# Time:2022/11/1 11:54 AM
#注册
from base.base_util import BaseUtil
from pageobject.signup_page import SignupPage


class TestSignup(BaseUtil):
    def test_signup(self):
    # 初始化对象
       sp=SignupPage(self.driver)
       sp.signup_page()