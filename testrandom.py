# author:lihua
# Time:2022/10/31 9:06 AM
import random
import string


class TestRandom:
    #获取随机整数
    def get_random_number(self):
        return random.randrange(81111111,89999999,1)
    #获取随机的由数字+字母组成的字段串
    def get_random_str(self,n):
        #n指定长度
        s = string.ascii_letters + string.ascii_uppercase + string.digits
        return ''.join(random.sample(s, n))


