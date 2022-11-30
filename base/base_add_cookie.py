# author:lihua
# Time:2022/11/4 9:22 AM
import json
import time
from time import sleep

from selenium import webdriver

from common.global_parameter import base_url


class BaseAddCookie():
    def setup(self) -> None:
        self.driver = webdriver.Chrome()
        driver = self.driver
        # 加载网页
        self.driver.get(base_url)
        print(self.driver.get_cookies())


        self.driver.delete_all_cookies()
        with open("./cookie.txt",'r',encoding="utf-8") as f:
            data = json.loads(f.read())
            print("data:",data)
        for i in data:
            cookie=self.driver.add_cookie(i)
        print("i",i)
        print("cookie",cookie)
        print(self.driver.get_cookies())
        sleep(3)
        self.driver.refresh()



    def tearup(self)-> None:
        self.driver.quit()
