# author:lihua
# Time:2022/11/15 3:27 PM
from selenium import webdriver

from base.base_util import BaseUtil
from common.global_parameter import poseidon_page
from pageobject.poseidon_page import PoseidonPage


class TestPoseidonPage():
    #analytics page
    def setup(self) ->None:
        global driver
        #打开浏览器
        self.driver = webdriver.Chrome()
        driver = self.driver
        #加载网页
        self.driver.get(poseidon_page)
        self.driver.maximize_window()
    def test_poseidon(self):

        pp=PoseidonPage(self.driver)
        pp.poseidon_page(searchname='cuci')