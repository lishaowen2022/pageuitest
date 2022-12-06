# author:lihua
# Time:2022/10/29 9:28 PM
#!/usr/bin/python
# -*- coding: UTF-8 -*-

import json
import time
from pprint import pprint

from selenium import webdriver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

from common.global_parameter import base_url


class BaseUtil:
    #设置全局的 driver

    def setup(self) ->None:
        global driver
        #实例化浏览器对象
        self.driver = webdriver.Chrome()

        driver = self.driver
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
