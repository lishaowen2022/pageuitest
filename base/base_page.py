# author:lihua
# Time:2022/10/26 4:05 PM
# author:lihua
# Time:2022/10/24 9:54 PM
import datetime
import os.path

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from base.base_util import BaseUtil


class BasePage(object):
    """
        BasePage封装了所有的公共方法，如driver/find_element...
    """

    def __init__(self,driver):
        # global driver
        self.driver = driver
        self.driver.maximize_window()



    # 定位元素
    # *loc 任意数量的位置参数
    def locator_element(self,loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver:self.driver.find_element(*loc).is_displayed())#设置显式等待时间
            return self.driver.find_element(*loc)
        except:
            print(u'%s can not find this element %s element' % (self.loc))
    def locator_elements(self,loc):
        try:
            WebDriverWait(self.driver, 10).until(lambda driver:self.driver.find_elements(*loc).is_displayed())
            return self.driver.find_elements(*loc)
        except:
            print('%s can not find this element %s element' % (self.loc))
    #获取文本的值
    def get_text(self,loc):
        return self.locator_element(loc).text
    #重构send_keys方法
    def send_keys(self,loc,value):
        self.locator_element(loc).send_keys(value)
    #重构 clear方法
    def clear(self,loc):
        self.locator_element(loc).clear()
    #重构下拉框操作
    def select(self,loc,value):
        sel=Select(self.locator_element(loc))
        # sel.select_by_visible_text(value)
        sel.select_by_value(value)
    #重构click方法
    def click(self,loc):
        self.locator_element(loc).click()

    #frame 切换
    def switch_to_frame(self,frame_name):
        self.driver.switch_to.frame(frame_name)
    #frame 切换回默认
    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

    #切换窗口
    def switch_to_window(self,title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if title==self.driver.title:
                break
    #截屏
    def save_screenshot(self,filename):
        self.driver.save_screenshot(filename)
    #截屏，指定文件路径
    def get_screenshot_as_file(self,filename):
        pro_dir=os.path.abspath(os.path.join(os.path.dirname((__file__),"..")))#获取当前项目的根目录
        screenshot_dir = os.path.join(pro_dir,"screenshot")#根目录下创建文件夹 screenshot
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)#不存在则创建截屏文件夹
        data_file=datetime.datetime.now().strftime('%Y%m%d')#当前日期
        screenshot_today_dir=os.path.join(screenshot_dir,data_file)#当前日期文件夹
        if not os.path.exists(screenshot_today_dir):
            os.makedirs(screenshot_today_dir)#不存在则创建当前日期文件夹
        now_time=datetime.datetime.now().strftime('%H%M%S')#时间戳
        filename=f'{filename}_{now_time}.png' #拼接文件名 文件名+时间戳+.png
        filepath=os.path.join(screenshot_today_dir,filename)
        self.driver.get_screenshot_as_file(filepath)
    #判断元素是否存在
    def check_element(self,value):
        return self.locator_element(value)
    #执行js脚本
    def script(self,src):
        self.driver.execute_script(src)








