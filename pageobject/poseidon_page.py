# author:lihua
# Time:2022/11/15 3:17 PM
from time import sleep

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from common.global_parameter import email
from testrandom import TestRandom


class PoseidonPage(BasePage):
    #页面元素
    search_loc=(By.CLASS_NAME,'meta-SNK-Search')
    like_loc=(By.CLASS_NAME,'meta-SNK-Like')
    search_input_loc=(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/input')
    cancel_btn_loc=(By.CLASS_NAME,'batal')
    store_product_loc=(By.CLASS_NAME,'store-bar')
    share_loc=(By.CLASS_NAME,'meta-SNK-Share')
    goto_store_btn_loc=(By.CLASS_NAME,'gotoStore')
    close_store_btn_loc=(By.XPATH,'//*[@id="__layout"]/div/div/div[3]/div/div[1]/div/div/div/div[1]/i')
    change_page_btn_loc=(By.CLASS_NAME,'meta-daohangmoren')
    sub_page_loc=(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[1]/div[2]/div/div/div[3]')
    main_page_loc=(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[1]/div[2]/div/div/div[2]')
    name_input_loc=(By.XPATH,'//*[@class="item-input"][1]')
    phone_input_loc=(By.XPATH,'//*[@type="number"]')
    email_input_loc=(By.XPATH,'//*[@id="whiteboard"]/div[6]/div/div[2]/div[3]/input')
    message_input_loc=(By.XPATH,'//*[@id="whiteboard"]/div[6]/div/div[2]/div[4]/div[2]/textarea')
    question_input_loc=(By.XPATH,'//*[@id="whiteboard"]/div[6]/div/div[2]/div[5]/input')
    form_sumit_btn_loc=(By.XPATH,'//*[@id="whiteboard"]/div[6]/div/div[2]/div[7]')

    def poseidon_page(self,searchname):
        #点击收藏
        self.click(self.like_loc)
        #点击搜索
        self.click(self.search_loc)
        #输入搜索内容
        self.send_keys(self.search_input_loc,searchname)
        sleep(3)
        #点击取消
        self.click(self.cancel_btn_loc)
        #查看store product
        self.click(self.store_product_loc)
        self.click(self.goto_store_btn_loc)
        # 获取所有窗口的句柄
        handles = self.driver.window_handles
        # 切换到最新窗口，-1为最新窗口的句柄
        self.driver.switch_to.window(handles[-1])
        sleep(3)
        #关闭新弹出的页面
        self.driver.close()
        #切换回原来页面
        self.driver.switch_to.window(handles[0])
        #关闭store product弹窗
        self.click(self.close_store_btn_loc)
        #点击切换页面
        self.click(self.change_page_btn_loc)
        # #查看子页面
        sleep(3)
        self.click(self.sub_page_loc)
        #点击切换页面
        sleep(3)
        self.click(self.change_page_btn_loc)
        #切回主page
        sleep(3)
        self.click(self.main_page_loc)
        sleep(3)
        #1.设置javascript脚本控制滚动条
        js_down = "window.scrollBy(0,100)" #(0:左边距，1000：上边距：单位像素)
        #2.selenium调用执行javascript脚本的方法
        sleep(3)
        self.driver.execute_script(js_down)
        #表单填写
        name = TestRandom().get_random_str(6)
        self.send_keys(self.name_input_loc,name)
        phone=TestRandom().get_random_number()
        self.send_keys(self.phone_input_loc,phone)
        self.send_keys(self.email_input_loc,email)
        message = TestRandom().get_random_str(20)
        self.send_keys(self.message_input_loc,message)
        question=name = TestRandom().get_random_str(10)
        self.send_keys(self.question_input_loc,question)
        sleep(3)
        self.click(self.form_sumit_btn_loc)










