# author:lihua
# Time:2022/10/31 5:40 PM
import string

import pytest
from selenium.webdriver.common.by import By

from base.base_page import BasePage



class SettingsPage(BasePage):
    #元素定位
    settings_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div[5]/div[1]/span')
    #analytics button loc
    analytics_btn_close_loc=(By.CLASS_NAME,'dp-switch')
    analytics_btn_open_loc=(By.XPATH,'//*[@class="dp-switch is-checked"]')
    confirm_close_btn_loc=(By.XPATH,'/html/body/section[1]/section/section/div/div[3]/button[2]')
    #语言下拉框定位
    selected_loc=(By.CLASS_NAME,'dp-select-drop-selection-rendered')
    #下拉框语言定位
    bahasa_language_loc=(By.XPATH,'(//*[@class="language-select-down-panel-item"])[1]')
    english_language_loc=(By.XPATH,'(//*[@class="language-select-down-panel-item"])[2]')
    # #ins开关
    # ins_disconnect_btn_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[1]/div/button')
    # ins_confirm_btn_loc=(By.XPATH,'/html/body/section[2]/section/section/div/div[3]/button[2]')
    # ins_allow_btn_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]')
    # ins_account_loc=(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
    # ins_password_loc=(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
    # ins_login_btn_loc=(By.CLASS_NAME,'_acan _acap _acas')
    def settings_page(self):

        # settings page操作
        self.click(self.settings_loc)

        #切换analytics开关
        self.click(self.analytics_btn_close_loc)
        self.click(self.confirm_close_btn_loc)
        self.click(self.analytics_btn_open_loc)
        self.click(self.selected_loc)
        self.click(self.bahasa_language_loc)
        self.click(self.english_language_loc)

        # #ins开关
        #
        # # self.click(self.ins_disconnect_btn_loc)
        # # self.click(self.ins_confirm_btn_loc)
        #
        # self.click(self.ins_disconnect_btn_loc)
        # # self.click(self.ins_btn_loc)
        # # 获取所有窗口的句柄
        # handles = self.driver.window_handles
        # # 切换到最新窗口，-1为最新窗口的句柄
        # self.driver.switch_to.window(handles[-1])
        # # self.click(self.ins_allow_btn_loc)
        # self.send_keys(self.ins_account_loc, insAccount)
        # self.send_keys(self.ins_password_loc, pwd)
        # self.click(self.ins_login_btn_loc)

