#!/user/bin/env python
#!encoding=utf-8
import time
import unittest
from Common.XmlTools import XmlTools
from Common.LogTools import Logger
from Common import LoginAction
from Page.BasePage import setBrowser
from Page.TongXun_Page.TongXunPage import TongXunPage

'''126邮箱通讯录测试'''

class TongXunTest(unittest.TestCase):
    '''126邮箱通讯录测试'''
    def setUp(self):
        self.get_xml = XmlTools()
        self.driver = setBrowser(self.get_xml.get_node_text('Common/browser'))
        self.url=LoginAction.seturl
        self.tongxun_page=TongXunPage(self.driver,self.url)
        LoginAction.login_action(self.tongxun_page)
        time.sleep(3)
        self.tongxun_page.go_TongXun()
        time.sleep(3)
        self.tongxun_page.clickCreatePeople()
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()

    def test_tongxun_001(self):
        '''正流程:创建删除联系人'''
        data=self.get_xml.make_child_data('TongXunPage/test1')
        self.log=Logger()
        self.log.info(u'126邮箱通讯录测试')
        self.log.info('=========================')
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #创建联系人
        self.tongxun_page.inputCreateName(data['name'])
        self.tongxun_page.inputEamil(data['email_addr'])
        self.tongxun_page.inputTel(data['telnum'])
        self.tongxun_page.inputBeiZhu(data['beizhu'])
        self.tongxun_page.submit()
        time.sleep(3)
        try:
            self.tongxun_page.assert_text_in_element(self.tongxun_page.email_loc,data['assert1'])
            self.log.info(u'联系人创建成功，信息如下:')
            self.log.info(u'创建姓名:%s'%data['name'])
            self.log.info(u'创建邮箱地址:%s'%data['email_addr'])
            self.log.info(u'创建电话号码:%s'%data['telnum'])
            self.log.info(u'创建备注信息:%s'%data['beizhu'])
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.tongxun_page.getImageFile(data['description'])
            raise

        #删除联系人
        self.tongxun_page.all_choose()
        self.tongxun_page.deletePeople()
        self.tongxun_page.acceptDelete()
        try:
            self.tongxun_page.assert_text_in_element(self.tongxun_page.tip_loc,data['assert2'])
            self.log.info(u'执行成功')
            self.log.info('*************************')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.tongxun_page.getImageFile(data['description'])
            raise

    def test_tongxun_002(self):
        '''异常流程:创建联系人不输入任何信息'''
        data = self.get_xml.make_child_data('TongXunPage/test2')
        self.log = Logger()
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.tongxun_page.submit()
        try:
            self.tongxun_page.assert_equal(self.tongxun_page.get_tip_error(),data['assert'])
            self.log.info(u'执行成功')
            self.log.info('*************************')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.tongxun_page.getImageFile(data['description'])
            raise

    def test_tongxun_003(self):
        '''异常流程:创建联系人只输入姓名'''
        data = self.get_xml.make_child_data('TongXunPage/test3')
        self.log = Logger()
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        # 执行操作
        self.tongxun_page.inputCreateName(data['name'])
        self.tongxun_page.submit()
        try:
            self.tongxun_page.assert_equal(self.tongxun_page.get_tip_error(), data['assert'])
            self.log.info(u'执行成功')
            self.log.info('*************************')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.tongxun_page.getImageFile(data['description'])
            raise

    def test_tongxun_004(self):
        '''异常流程:创建联系人只输入手机号码'''
        data = self.get_xml.make_child_data('TongXunPage/test4')
        self.log = Logger()
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.tongxun_page.inputTel(data['telnum'])
        self.tongxun_page.submit()
        try:
            self.tongxun_page.assert_equal(self.tongxun_page.get_tip_error(), data['assert'])
            self.log.info(u'执行成功')
            self.log.info('*************************')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('*************************')
            self.tongxun_page.getImageFile(data['description'])
            raise

    def test_tongxun_005(self):
        '''异常流程:创建联系人只输入姓名手机号码'''
        data = self.get_xml.make_child_data('TongXunPage/test5')
        self.log = Logger()
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        # 执行操作
        self.tongxun_page.inputCreateName(data['name'])
        self.tongxun_page.inputTel(data['telnum'])
        self.tongxun_page.submit()
        try:
            self.tongxun_page.assert_equal(self.tongxun_page.get_tip_error(), data['assert'])
            self.log.info(u'执行成功')
            self.log.info('=========================')
        except Exception:
            self.log.error(u'执行失败')
            self.log.info('=========================')
            self.tongxun_page.getImageFile(data['description'])
            raise


if __name__=="__main__":
    unittest.main()