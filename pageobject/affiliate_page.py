# author:lihua
# Time:2022/11/10 4:40 PM
from time import sleep

from selenium.webdriver.common.by import By

from base.base_page import BasePage

#分析页面


class AffiliatePage(BasePage):
    #页面元素定位
    affiliate_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div[4]/div[1]/span')
    search_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[2]/div/div/input')
    search_btn_loc=(By.CLASS_NAME,'product-search-button')
    affiliate_img_loc=(By.XPATH,'//*[@id="app"]/div/div[2]/div[2]/div[2]/div/div[2]/div[4]/div/div[1]/div[1]/img')
    affiliate_url_loc=(By.XPATH,'/html/body/section[1]/section/section/div/div[2]/div[3]/div/div/div/input')
    generate_btn_loc=(By.XPATH,'//*[@class="dp-btn is-primary is-middle main-btn"]')
    copy_url_loc=(By.CLASS_NAME,'generator-form-copy')
    close_window_loc=(By.XPATH,'/html/body/section[1]/section/header/div/i')
    def affiliate_page(self,url,product):

        # analytics page操作
        self.click(self.affiliate_loc)
        #联盟生成短链
        self.click(self.affiliate_img_loc)
        self.send_keys(self.affiliate_url_loc,url)
        self.click(self.generate_btn_loc)
        self.click(self.copy_url_loc)
        self.click(self.close_window_loc)
        #搜索商品
        self.send_keys(self.search_loc,product)
        self.click(self.search_btn_loc)
        self.clear(self.search_loc)

    def assert_txt(self, t):
        user_name = self.get_text(self.username_btn_loc)
        assert t in user_name



