# author:lihua
# Time:2022/11/15 3:17 PM
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PoseidonPage(BasePage):
    #页面元素
    search_loc=(By.CLASS_NAME,'meta-SNK-Search')
    like_loc=(By.CLASS_NAME,'meta-SNK-Like')
    search_input_loc=(By.XPATH,'//*[@id="__layout"]/div/div/div[1]/div[2]/div[1]/div[2]/div/div/div[1]/div/div/input')
    cancel_btn_loc=(By.CLASS_NAME,'batal')

    def poseidon_page(self,searchname):
        #点击收藏
        self.click(self.like_loc)
        #点击搜索
        self.click(self.search_loc)
        #输入搜索内容
        self.send_keys(self.search_input_loc,searchname)
        #点击取消
        self.click(self.cancel_btn_loc)







