#!/user/bin/env python
#!encoding=utf-8
import time
import unittest
from Common.LogTools import Logger
from Page.BasePage import setBrowser
from Common import LoginAction
from Common.XmlTools import XmlTools
from Page.HongQiEmail_Page.HongQiEmailPage import HongQiEmailPage

'''126邮箱红旗邮件测试'''

class HongQiTest(unittest.TestCase):
    '''126邮箱红旗邮件测试'''
    def setUp(self):
        self.get_xml = XmlTools()
        self.driver = setBrowser(self.get_xml.get_node_text('Common/browser'))
        self.url=LoginAction.seturl
        self.hongqi_page=HongQiEmailPage(self.driver,self.url)
        LoginAction.login_action(self.hongqi_page)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_hongqi(self):
        '''正流程:设定旗帜颜色'''
        data=self.get_xml.make_child_data('HongQiEmailPage')
        self.log=Logger()
        self.log.info(u'126邮箱红旗邮件测试')
        self.log.info('=========================')
        self.log.info(u'执行开始')

        #执行操作
        self.hongqi_page.go_hongqi()
        self.hongqi_page.click_qita_button()
        time.sleep(3)
        color=self.hongqi_page.click_qizhi_color()
        self.log.info(u'选择的旗帜是【%s】'%color)
        try:
            self.hongqi_page.assert_text_in_element(self.hongqi_page.tip_loc,u'没有设置 %s邮件哦，您可以：'%color)
            self.log.info(u'执行成功')
            self.log.info('=========================')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('=========================')
            self.hongqi_page.getImageFile(data['description'])

if __name__=="__main__":
    unittest.main()