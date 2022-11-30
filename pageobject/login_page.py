# author:lihua
# Time:2022/10/26 4:06 PM
# author:lihua
# Time:2022/10/24 10:02 PM
"""
   page_object主要是放页面的元素和页面的动作
"""
import json
from pprint import pprint
from time import sleep
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.devtools.v104 import browser

from base.base_page import BasePage

#登录
# from common.global_parameter import phone, code, base_url


class LoginPage(BasePage):
    #页面的元素
    homepage_loc=(By.CLASS_NAME,"active-login-item")
    phone_loc=(By.CLASS_NAME,"el-input__inner")
    login_btn=(By.CLASS_NAME,"login-btn")
    code_loc=(By.XPATH,"(//div//input)[2]")
    # username_loc = (By.CLASS_NAME, "meta-header-user")
    # logout_loc=(By.CLASS_NAME,"profile-logout")

    change_to_email_loc=(By.CLASS_NAME,"change-action")
    input_email_loc=(By.CLASS_NAME,"el-input__inner")
    google_loc=(By.CLASS_NAME,"loginIcon")
    google_email_loc=(By.XPATH,'//*[@id="identifierId"]')
    next_step_btn_loc=(By.XPATH,'(//*[@class="VfPpkd-vQzf8d"])[2]')
    facebook_loc=(By.XPATH,'(//div/div)[18]')

    facebook_email_loc=(By.XPATH,'//*[@id="email"]')
    facebook_email_pwd_loc=(By.XPATH,'//*[@id="pass"]')
    facebook_login_btn_loc=(By.XPATH,'//*[@name="login"]')
    username_btn_loc=(By.CLASS_NAME,'user-name')

    #页面的动作
    #手机号登录
    def login_page_use_mobile(self,phone,code):
        self.click(self.homepage_loc)
        self.send_keys(self.phone_loc,phone)
        self.click(self.login_btn)
        self.send_keys(self.code_loc,code)


        # self.click(self.username_loc)

    # def get_login_cookie(self,driver):
    #     cookies = self.driver.get_cookies()  # 获取目前所有的cookies
    #     pprint(cookies)
    #     sleep(3)
    #
    #     with open("./cookie.txt", "w+",encoding="utf-8") as f:
    #         # f.write(json.dumps(cookies))  # 将目前所有的cookies存储到文件中
    #           json.dump(cookies,f)
    #
    #
    #     self.driver.delete_all_cookies()
    # 三方登录-google
    def login_page_use_google(self,email):
        self.click(self.homepage_loc)
        self.click(self.google_loc)
        # 获取所有窗口的句柄
        handles = self.driver.window_handles
        # 切换到最新窗口，-1为最新窗口的句柄
        self.driver.switch_to.window(handles[-1])
        self.send_keys(self.google_email_loc,email)
        self.click(self.next_step_btn_loc)
    #三方登录-facebook
    def login_page_use_facebook(self,email,pwd):
        self.click(self.homepage_loc)
        self.click(self.facebook_loc)
        #获取所有窗口的句柄
        handles = self.driver.window_handles
        #切换到最新窗口，-1为最新窗口的句柄
        self.driver.switch_to.window(handles[-1])
        self.send_keys(self.facebook_email_loc,email)
        self.send_keys(self.facebook_email_pwd_loc,pwd)
        self.click(self.facebook_login_btn_loc)
        self.driver.switch_to.window(handles[0])
    #使用邮箱登录
    def login_use_email(self,email,code):
        self.click(self.homepage_loc)
        self.click(self.change_to_email_loc)
        self.send_keys(self.input_email_loc,email)
        self.click(self.login_btn)
        self.send_keys(self.code_loc, code)
    def assert_txt(self,t):
        user_name=self.get_text(self.username_btn_loc)
        assert t in user_name


