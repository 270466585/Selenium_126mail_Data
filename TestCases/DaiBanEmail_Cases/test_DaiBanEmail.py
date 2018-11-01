#!/user/bin/env python
#!encoding=utf-8
import time
import unittest
from Common.LogTools import Logger
from Common.XmlTools import XmlTools
from Common import LoginAction
from Page.BasePage import setBrowser
from Page.DaiBanEmail_Page.DaiBanEmailPage import DaiBanPage

'''126邮箱待办邮件测试'''

class DaiBanTest(unittest.TestCase):
    '''126邮箱待办邮件测试'''
    def setUp(self):
        self.get_xml=XmlTools()
        self.driver=setBrowser(self.get_xml.get_node_text('Common/browser'))
        self.url=LoginAction.seturl
        self.daiban_page=DaiBanPage(self.driver,self.url)
        LoginAction.login_action(self.daiban_page)
        time.sleep(3)
        self.daiban_page.go_daiban()
        time.sleep(1)

    def tearDown(self):
        self.driver.quit()

    def test_daiban(self):
        '''正流程:进入待办邮件模块并刷新'''
        data=self.get_xml.make_child_data('DaiBanPage')
        self.log = Logger()
        self.log.info(u'126邮箱待办邮件测试')
        self.log.info('=========================')
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.daiban_page.clickRefresh()
        try:
            time.sleep(5)
            self.daiban_page.assert_equal(self.daiban_page.get_tip(), data['assert'])
            self.log.info(u'执行成功')
            self.log.info('=========================')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('=========================')
            self.daiban_page.getImageFile(data['description'])
            raise

