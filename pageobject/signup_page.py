# author:lihua
# Time:2022/10/31 6:10 PM
from time import sleep
from turtle import title

from selenium.webdriver.common.by import By

from base.base_page import BasePage

#注册
from common.global_parameter import email, fullname, link_account, ins_account, facebook_account
from testrandom import TestRandom


class SignupPage(BasePage):
    #元素定位
    homepage_sign_up_btn_loc=(By.CLASS_NAME,'action-item')
    # sign_up_btn_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/span')
    phone_loc=(By.CLASS_NAME,'el-input__inner')
    signup_btn_loc=(By.CLASS_NAME,'signup-btn')
    code_loc=(By.XPATH,'(//div//input)[2]')
    #personal information page
    email_loc=(By.XPATH,'//*[@id="app"]/div/div[3]/div/div[2]/div/div[3]/div[4]/input')
    fullname_loc=(By.XPATH,'//*[@id="app"]/div/div[3]/div/div[2]/div/div[3]/div[6]/input')
    create_account_loc=(By.XPATH,'//*[@id="app"]/div/div[3]/div/div[2]/div/button/span')
    #onboarding page
    model_select_loc=(By.XPATH,'//*[@id="app"]/div/div/div[3]/div[2]/div/div[1]')
    profile_start_btn_loc=(By.CLASS_NAME,'profile-start-btn')
    link_input_loc=(By.XPATH,'(//div/input)[1]')
    ins_input_loc=(By.XPATH,'(//div/input)[2]')
    facebook_input_loc=(By.XPATH,'(//div/input)[3]')
    continue_btn_loc=(By.CLASS_NAME,'link-button-ordinary')
    page_title_input_loc=(By.CLASS_NAME,'url-input-enter')
    page_publish_btn_loc=(By.CLASS_NAME,'url-button-ordinary')
    update_btn_loc=(By.CLASS_NAME,'button-publish')
    preview_btn_loc=(By.CLASS_NAME,'btn-preview')
    dashboard_btn_loc=(By.CLASS_NAME,'btn-dashboard')

    def signup_page(self,phone=TestRandom().get_random_number()):
        self.click(self.homepage_sign_up_btn_loc)
        self.send_keys(self.phone_loc,phone)
        self.click(self.signup_btn_loc)
        if phone%2==0:
            code='0000'
        else:
            code='1111'
        self.send_keys(self.code_loc,code)
        self.send_keys(self.email_loc,email)
        self.send_keys(self.fullname_loc,fullname)
        self.click(self.create_account_loc)
        self.click(self.model_select_loc)
        self.click(self.profile_start_btn_loc)
        self.send_keys(self.link_input_loc,link_account)
        self.send_keys(self.ins_input_loc,ins_account)
        self.send_keys(self.facebook_input_loc,facebook_account)
        self.click(self.continue_btn_loc)
        title=TestRandom().get_random_str(6)
        self.send_keys(self.page_title_input_loc,title)
        sleep(5)
        self.click(self.page_publish_btn_loc)
        sleep(5)
        self.click(self.update_btn_loc)
        #查看波塞冬页面
        sleep(5)
        self.click(self.preview_btn_loc)
        sleep(5)
        #返回 dashboard
        self.click(self.dashboard_btn_loc)






