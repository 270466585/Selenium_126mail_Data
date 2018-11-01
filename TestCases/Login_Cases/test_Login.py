#!/user/bin/env python
#!encoding=utf-8
import time
import unittest
from Page.Login_Page.LoginPage import LoginPage
from Page.BasePage import setBrowser
from Common.XmlTools import XmlTools
from Common.LogTools import Logger

class LoginTest(unittest.TestCase):
    '''126邮箱登录测试'''
    def setUp(self):
        self.get_xml = XmlTools()
        self.driver = setBrowser(self.get_xml.get_node_text('Common/browser'))
        self.url=self.get_xml.get_node_text('Common/login/url')
        self.login_page=LoginPage(self.driver,self.url)
        self.login_page.open()
        self.login_page.maximize()
        self.login_page.changeIframe(self.get_xml.get_node_text('LoginPage/iframe'))

    def tearDown(self):
        self.driver.quit()

    def test_login_001(self):
        '''正流程:输入正确的账号密码'''
        data=self.get_xml.make_child_data('LoginPage/test1')
        self.log=Logger()
        self.log.info(u'126邮箱登录测试')
        self.log.info('=========================')
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.login_page.inputUsername(data['login_username'])
        self.login_page.inputPassword(data['login_password'])
        self.login_page.submit()
        time.sleep(5)
        try:
            self.login_page.assert_text_in_element(self.login_page.user_loc,data['assert'])
            self.log.info(u'执行成功')
            self.log.info('*************************')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.login_page.getImageFile(data['description'])
            raise

    def test_login_002(self):
        '''异常流程:账号密码都不输入'''
        data=self.get_xml.make_child_data('LoginPage/test2')
        self.log = Logger()
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.login_page.submit()
        time.sleep(5)
        try:
            self.login_page.assert_equal(self.login_page.get_error(),data['assert'])
            self.log.info('执行成功')
            self.log.info('*************************')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.login_page.getImageFile(data['description'])
            raise

    def test_login_003(self):
        '''异常流程:输入账号不输密码'''
        data=self.get_xml.make_child_data('LoginPage/test3')
        self.log = Logger()
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.login_page.inputUsername(data['login_username'])
        self.login_page.submit()
        time.sleep(5)
        try:
            self.login_page.assert_equal(self.login_page.get_error(),data['assert'])
            self.log.info('执行成功')
            self.log.info('*************************')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.login_page.getImageFile(data['description'])
            raise

    def test_login_004(self):
        '''异常流程:输入账号密码输入错误'''
        data=self.get_xml.make_child_data('LoginPage/test4')
        self.log = Logger()
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.login_page.inputUsername(data['login_username'])
        self.login_page.inputPassword(data['login_password'])
        self.login_page.submit()
        time.sleep(5)
        try:
            self.login_page.assert_equal(self.login_page.get_error(),data['assert'])
            self.log.info('执行成功')
            self.log.info('=========================')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('=========================')
            self.login_page.getImageFile(data['description'])
            raise

if __name__=="__main__":
    unittest.main()
