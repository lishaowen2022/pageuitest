# author:lihua
# Time:2022/10/31 4:39 PM
import pytest
from selenium.webdriver.common.by import By

from base.base_page import BasePage

#分析页面


class AnalyticsPage(BasePage):
    #页面元素定位
    analytics_loc=(By.XPATH,'//*[@id="app"]/div/div[1]/div/div[2]/div[2]/div[1]/span')
    selected_loc=(By.CLASS_NAME,'dp-select-button')
    seven_days_loc=(By.XPATH,'/html/body/div[2]/ul/li[1]')
    one_month_loc=(By.XPATH,'/html/body/div[2]/ul/li[2]')
    three_month_loc=(By.XPATH,'/html/body/div[2]/ul/li[3]')


    def analytics_page(self):

        # analytics page操作
        self.click(self.analytics_loc)
        self.click(self.selected_loc)
        self.click(self.seven_days_loc)
        self.click(self.selected_loc)
        self.click(self.one_month_loc)
        self.click(self.selected_loc)
        self.click(self.three_month_loc)






