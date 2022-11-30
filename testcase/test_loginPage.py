# author:lihua
# Time:2022/10/26 4:06 PM

#测试用例层：存放测试用例以及测试数据
import unittest
from time import sleep

import pytest
from ddt import ddt, data, unpack

from base.base_util import BaseUtil
from common.global_parameter import base_url, login_code, login_email, password
from pageobject.login_page import LoginPage

# @ddt

class TestLogin(BaseUtil):
    #登录
    #*表示把会读取到的excel数据最外层的[]去掉，并且会根据读取的数据条数对应执行多次
    # @data(*ExcelUtil().read_excel())
    # @unpack
    # @pytest.mark.parametrize("index,phone,code",ExcelUtil().read_excel())
    #手机号登录
    def test_login_use_phone(self):
        #初始化对象
        # print(datainfo)
        # self.driver.get(base_url)
        lp=LoginPage(self.driver)
        lp.login_page_use_mobile(phone='811112222',code=login_code)
        #结果校验，登录成功用户名校验
        lp.assert_txt('aaa')
        # lp.get_login_cookie(self.driver)
        #unittest断言
        # self.assertEqual(lp.get_except_result(),'')
        # #pytest断言
        # assert lp.get_except_result() is True
    def test_login_use_email(self):
        lp = LoginPage(self.driver)
        lp.login_use_email(email=login_email,code=login_code)
        # 结果校验，登录成功用户名校验
        lp.assert_txt('HuaLi')


    # 三方登录-google
    def test_login_use_google(self):
        lp=LoginPage(self.driver)
        lp.login_page_use_google(email=login_email)

    # 三方登录-facebook
    def test_login_use_facebook(self):
        lp=LoginPage(self.driver)
        lp.login_page_use_facebook(email=login_email,pwd=password)
        # 结果校验，登录成功用户名校验
        lp.assert_txt('HuaLi')


