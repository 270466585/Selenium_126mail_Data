#!/user/bin/env python
#!encoding=utf-8
import time
import unittest
from Page.BasePage import setBrowser
from Page.SendEmail_Page.SendEmailPage import SendEmailPage
from Common.XmlTools import XmlTools
from Common import LoginAction
from Common.LogTools import Logger

'''126邮箱发送邮件测试'''

class SendEmailTest(unittest.TestCase):
    '''126邮箱发送邮件测试'''
    def setUp(self):
        self.get_xml = XmlTools()
        self.driver=setBrowser(self.get_xml.get_node_text('Common/browser'))
        self.url=LoginAction.seturl
        self.sendemail_page=SendEmailPage(self.driver,self.url)
        LoginAction.login_action(self.sendemail_page)
        time.sleep(3)
        self.sendemail_page.go_xiexin()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

    def test_sendemail_001(self):
        '''正流程:编写收件人、主题、内容'''
        data=self.get_xml.make_child_data('SendEmailPage/test1')
        self.log=Logger()
        self.log.info(u'126邮箱发送邮件测试')
        self.log.info('=========================')
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.sendemail_page.inputShouJianInfo(data['email_receiver'])
        self.sendemail_page.inputSubject(data['email_subject'])
        self.sendemail_page.changeIframe_element(self.sendemail_page.iframe_loc)
        self.sendemail_page.editText(data['email_text'])
        self.sendemail_page.changeIframeOut()
        self.sendemail_page.clickFaSongButton()
        time.sleep(3)
        try:
            self.sendemail_page.assert_text_in_element(self.sendemail_page.continue_sendemail_loc,data['assert'])
            self.log.info(u'执行成功')
            self.log.info('*************************')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.sendemail_page.getImageFile(data['description'])
            raise

    def test_sendemail_002(self):
        '''异常流程:收件人、主题、内容都不输入'''
        data=self.get_xml.make_child_data('SendEmailPage/test2')
        self.log = Logger()
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.sendemail_page.clickFaSongButton()
        time.sleep(3)
        try:
            self.sendemail_page.assert_equal(self.sendemail_page.get_error(),data['assert'])
            self.log.info(u'执行成功')
            self.log.info('*************************')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.sendemail_page.getImageFile(data['description'])
            raise

    def test_sendemail_003(self):
        '''异常流程:输入收件人内容不输入主题'''
        data=self.get_xml.make_child_data('SendEmailPage/test3')
        self.log=Logger()
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.sendemail_page.inputShouJianInfo(data['email_receiver'])
        self.sendemail_page.changeIframe_element(self.sendemail_page.iframe_loc)
        self.sendemail_page.editText(data['email_text'])
        self.sendemail_page.changeIframeOut()
        self.sendemail_page.clickFaSongButton()
        time.sleep(2)

        #判断提示框是否打开
        try:
            self.sendemail_page.assert_text_in_element(self.sendemail_page.tip_loc,data['assert1'])
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.sendemail_page.getImageFile(data['description'])
            raise
        self.sendemail_page.click_queding_button()
        time.sleep(5)

        #判断是否执行完成
        try:
            self.sendemail_page.assert_text_in_element(self.sendemail_page.continue_sendemail_loc, data['assert2'])
            self.log.info(u'执行成功')
            self.log.info('*************************')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.sendemail_page.getImageFile(data['description'])
            raise

    def test_sendemail_004(self):
        '''异常流程:输入内容不输入收件人主题'''
        data=self.get_xml.make_child_data('SendEmailPage/test4')
        self.log = Logger()
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        # 执行操作
        self.sendemail_page.changeIframe_element(self.sendemail_page.iframe_loc)
        self.sendemail_page.editText(data['email_text'])
        self.sendemail_page.changeIframeOut()
        self.sendemail_page.clickFaSongButton()
        try:
            self.sendemail_page.assert_equal(self.sendemail_page.get_error(),data['assert'])
            self.log.info(u'执行成功')
            self.log.info('=========================')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('=========================')
            self.sendemail_page.getImageFile(data['description'])
            raise

if __name__=="__main__":
    unittest.main()