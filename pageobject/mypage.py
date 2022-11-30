# author:lihua
# Time:2022/10/27 8:31 PM
#Manage页面
from time import sleep

import pytest
# from selenium.webdriver import ActionChains
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.by import By

from base.base_page import BasePage

from testrandom import TestRandom


class MyPage(BasePage):

   #页面元素定位
   manage_page_btn_loc=(By.CLASS_NAME,"manage")
   #第二个页面元素
   the_second_page_loc = (By.XPATH, "(//*[@class='item-content'])[3]")
   #第三个页面元素
   the_third_page_loc=(By.XPATH,"(//*[@class='item-content'])[5]")
   save_btn_loc=(By.CLASS_NAME,"saveBtn")
   wallet_entry_loc=(By.CLASS_NAME,'wallet-content')
   store_link_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[1]')
   omni_link_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[2]')
   menu_link_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/div[3]/div[2]/div[2]/div[3]')
   promo_link_loc=(By.CLASS_NAME,'operation-image')
   #创建子page元素定位
   add_page_btn_loc = (By.CLASS_NAME, "page-card-button")
   title_input_loc = (By.XPATH, "(//div/input)[8]")
   publish_btn_loc = (By.CLASS_NAME, "publish-dialog-btn")
   #edit page 元素定位
   add_heading_loc=(By.XPATH,'//*[@id="app"]/section/section[2]/section[1]/section/section[1]/section/ul[1]/li')
   title_input_loc=(By.CLASS_NAME,'text-edit-input')



   def my_page(self):

       #manage page操作
       self.click(self.manage_page_btn_loc)
       #subpage sorting
       action = ActionChains(self.driver)
       action.drag_and_drop(self.locator_element(self.the_second_page_loc),self.locator_element(self.the_third_page_loc)).perform()
       sleep(10)
       self.click(self.save_btn_loc)

       sleep(5)
       js_down="window.scrollTo(0,1000)"
       self.driver.execute_script(js_down)
       # self.click(self.wallet_entry_loc)
       # self.click(self.store_link_loc)
       # self.click(self.omni_link_loc)
       # self.click(self.menu_link_loc)
       # self.click(self.promo_link_loc)

       #创建子页面
       # self.click(self.add_page_btn_loc)
       # title = TestRandom().get_random_str(6)
       # sleep(5)
       # self.send_keys(self.title_input_loc,title)
       # sleep(5)
       # self.click(self.publish_btn_loc)
       # self.click(self.add_heading_loc)
       # self.click(self.title_input_loc,title)






