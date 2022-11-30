# author:lihua
# Time:2022/11/15 3:17 PM
import self
from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PoseidonPage(BasePage):
    search_loc=(By.CLASS_NAME,'meta-SNK-Search')

    def poseidon_page(self):
        self.click(self.search_loc)




