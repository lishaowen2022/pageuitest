# author:lihua
# Time:2022/10/29 11:00 AM
import os
import sys
sys.path.append('/var/jenkins_home/workspace/page/testcase')
#测试jenkins
import unittest


import pytest

if __name__ == '__main__':
    #执行需要的用例，并且生成HTML格式自动化的测试报告
    #使用unittest默认的测试用例的加载器去发现testcase目录下以py结尾的所有测试用例
    # suite = unittest.defaultTestLoader.discover("./testcase","*.py")
    # #生成html报告文件
    # report_file = open("./report/reports.html","wb")
    # #生成一个HTMLTestRunner运行器对象（必须下载一个文件HTMLTestRunner.py,放到python的lib目录下）
    # runner = HTMLTestRunner(stream=report_file,title="page测试报告",description="报告详情如下")
    # runner.run(suite)
    #第一步：生成json格式的临时文件：-vs:打印结果，./testcase：执行的测试用例，'--alluredir','./temp'：allure报告的临时文件，'--clean-alluredir'：每执行一次把临时文件清除
    pytest.main(['-vs','./testcase','--alluredir','./temp','--clean-alluredir'])
    #第二步：根据json格式临时文件生成allure报告
    os.system("allure generate ./temp -o ./report --clean")
