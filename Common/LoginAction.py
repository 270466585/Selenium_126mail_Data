#!/user/bin/env python
#!encoding=utf-8
from Page.Login_Page.LoginPage import LoginPage
from Common.XmlTools import XmlTools
'''单独封装登录操作，用于整个自动化测试'''

#获取xml文件登录数据配置
get_xml=XmlTools()
login_data=get_xml.make_child_data('Common/login')
seturl=login_data['url']

#封住登录操作
def login_action(self):
    self.login=LoginPage(self.driver,self.url)
    self.login.open()
    self.login.maximize()
    self.login.changeIframe(login_data['iframe'])
    self.login.inputUsername(login_data['login_username'])
    self.login.inputPassword(login_data['login_password'])
    self.login.submit()



