# author:lihua
# Time:2022/10/29 9:28 PM
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import time
import os
import sys
from pprint import pprint

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from common.global_parameter import base_url

#current_path = os.path.dirname(os.path.abspath(__file__))
system_driver = sys.platform




class BaseUtil:
    #设置全局的 driver

    def __get_chrome_driver(self):
        
        if system_driver.lower() == "linux":
            chrome_options = Options()
            chrome_options.add_argument('no-sandbox')
            chrome_options.add_argument("headless")
            chrome_options.add_argument('disable-dev-shm-usage')
            chrome_options.add_argument('disable-gpu')
            return driver



    def setup(self) ->None:

        global driver
        #实例化浏览器对象
        driver = self.driver
        self.driver = webdriver.Chrome()

        #driver = self.driver
        #加载网页
        self.driver.get(base_url)
        # cookies = driver.get_cookies()#获取目前所有的cookies
        # pprint(cookies)
        # time.sleep(3)
        #
        # with open("cookie.txt","w+") as f:
        #     f.write(json.dumps(cookies))#将目前所有的cookies存储到文件中
        # driver.delete_all_cookies()#删除内存中所有的cookies
    #
    def teardown(self) ->None:
        time.sleep(3)
        self.driver.quit()
