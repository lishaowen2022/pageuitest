# author:lihua
# Time:2022/10/28 10:32 AM
#退出登录
from time import sleep

import pyperclip
import pytest
from pynput.keyboard import Controller, Key
from selenium.webdriver.common.by import By

from base.base_page import BasePage
from common.global_parameter import img_url


class LogoutPage(BasePage):
    #页面元素定位

    username_loc=(By.CLASS_NAME,"meta-header-user")
    help_center_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/div[5]/div[1]')
    change_to_store_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/div[5]/div[2]')
    logout_loc=(By.CLASS_NAME,"profile-logout")
    account_setting_loc=(By.CLASS_NAME,'profile-setting-entry')
    change_photo_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[1]/div[3]/div[2]/div[2]/div/section/section/section/div/div[2]/button')
    upload_photo_loc=(By.XPATH,'(//div/input)[5]')
    #页面操作退出登录
    def logout_page(self):

        self.click(self.username_loc)
        self.click(self.help_center_loc)
        self.click(self.change_to_store_loc)
        # self.click(self.account_setting_loc)
        # self.click(self.change_photo_loc)
        # pyperclip.copy(img_url)
        # self.click(self.upload_photo_loc)
        # # 实例化键盘对象
        # keyboard = Controller()
        # # 模拟键盘按下Ctrl键,value就相当于+号,表示后面还有按键
        # sleep(3)
        # keyboard.press(Key.ctrl.value)
        # # 模拟键盘按下v键
        # sleep(3)
        # keyboard.press('x')
        # # 此时文件名的输入框已经完成了粘贴操作，我们需要释放掉ctrl键和v键
        # sleep(3)
        # keyboard.release(Key.ctrl.value)
        # sleep(3)
        # keyboard.release('x')
        # # 模拟按下Enter键后释放Enter键，就大功告成了！
        # sleep(3)
        # keyboard.press(Key.enter)
        # sleep(3)
        # keyboard.release(Key.enter)
        # self.click(self.upload_photo_loc)
        # self.send_keys(self.upload_photo_loc,r"/Users/lihua/Documents/desty/img/9541bf5f3d035be57bc03f2eb4935e55.jpeg")





        self.click(self.logout_loc)
