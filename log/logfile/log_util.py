# author:lihua
# Time:2022/11/16 4:13 PM
import logging
import os
from time import strftime,localtime
# 使用类的方式实现日志的输出和调用
class LogFileOperation():
    def __init__(self,logger=None):
        self.logger = logging.getLogger("logger")
        self.logger.setLevel(logging.DEBUG)#全局日志等级
        #避免日志重复输出
        if not self.logger.handlers:
            pro_path = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
            self.alllogPath = os.path.join(pro_path, '../log/logfile', 'AllLogs', "")#打开全部日志存放路径
            self.errorlogpath = os.path.join(pro_path, '../log/logfile', 'ErrorLogs', "")#打开错误日志存放路径

            # self.sysTime = strftime('%Y%m%d%H%M%S', localtime())#获取当前系统时间
            self.alllog_name = self.alllogPath + "allLog.log"  #定义全部日志文件名
            self.errorlog_name = self.errorlogpath  +"errorLog.log"  #定义错误日志文件名
            print("所有日志路径："+self.alllog_name,"\n错误日志路径："+self.errorlog_name)

            # # 创建一个handler，用于写入日志文件，参数为打开的文件的路径、名字等信息，以及打开的方式
            allfh = logging.FileHandler(self.alllog_name,'a', encoding="utf-8")
            allfh.setLevel(logging.DEBUG)#定义全部日志等级
            errorfh = logging.FileHandler(self.errorlog_name,'a', encoding="utf-8")
            errorfh.setLevel(logging.ERROR)#定义错误日志等级

            # 再创建一个handler，用于输出到控制台
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义输出的格式，formatter 此处定义输出日志生成时间、当前执行文件名、日志等级、输出信息
            formatter = logging.Formatter(fmt='%(asctime)s - %(filename)s - %(levelname)s - %(message)s'
                                          )
            allfh.setFormatter(formatter)#给全部日志传入输出格式
            errorfh.setFormatter(formatter)#给错误日志传入输出格式
            ch.setFormatter(formatter)

            self.logger.addHandler(allfh)
            self.logger.addHandler(errorfh)
            self.logger.addHandler(ch)

            allfh.close()
            errorfh.close()
            ch.close()

# logger = LogFileOperation().get_log()
    def get_log(self):
        return self.logger
if __name__ == '__main__':
    logger = LogFileOperation().get_log()