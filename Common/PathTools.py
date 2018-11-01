#!/user/bin/env python
#!encoding=utf-8
'''路径管理'''
import os

#根目录
root_path=os.path.dirname(__file__)
#数据路径
data_path=r'D:\\PyCharm\\Project\\WEBautotest\\Selenium_126mail_Data\\Data\\data.xml'
#截图路径
image_path=root_path.replace("\\","/").replace("/Common","/Image/")
#日志路径
log_path=root_path.replace("\\","/").replace("/Common","/Log/")
#报告路径
report_path=root_path.replace("\\","/").replace("/Common","/Report/")
