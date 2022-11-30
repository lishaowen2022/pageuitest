# author:lihua
# Time:2022/10/31 5:49 PM
from time import sleep

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from base.base_page import BasePage



class WalletPage(BasePage):
    #页面元素定位
    wallet_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div[3]/div[1]/span')
    mengerti_btn_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[8]/div/div/div/div[2]/button/span')
    withdraw_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div[3]/div[1]/div[1]/div[2]/button/span')
    withdraw_amount_loc=(By.XPATH,'//div/input')
    withdraw_btn_loc =(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[1]/div[2]/form/button/span')
    confirm_withdraw_btn_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div/div[2]/div/div/div/div[3]/span/button[2]/span')
    def wallet_page(self,amount):


        # wallet page操作
        self.click(self.wallet_loc)
        #切换窗口
        # 获取所有窗口的句柄
        handles = self.driver.window_handles
        # 切换到最新窗口，-1为最新窗口的句柄
        self.driver.switch_to.window(handles[-1])
        self.click(self.mengerti_btn_loc)
        self.click(self.withdraw_loc)
        sleep(10)
        self.send_keys(self.withdraw_amount_loc,amount)
        self.click(self.withdraw_btn_loc)
        self.click(self.confirm_withdraw_btn_loc)



