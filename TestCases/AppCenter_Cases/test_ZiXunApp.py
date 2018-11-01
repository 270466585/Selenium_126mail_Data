#!/user/bin/env python
#!encoding=utf-8
import time
import unittest
from Common.XmlTools import XmlTools
from Common.LogTools import Logger
from Page.BasePage import setBrowser
from Common import LoginAction
from Page.AppCenter_Page.AppCenterPage import AppCenterPage

'''126邮箱应用中心咨询类app测试'''

class ZiXunAppTest(unittest.TestCase):
    '''126邮箱应用中心app测试'''
    @classmethod
    def setUpClass(cls):
        cls.get_xml=XmlTools()
        cls.driver=setBrowser(cls.get_xml.get_node_text('Common/browser'))
        cls.url=LoginAction.seturl
        cls.zixunapp_page=AppCenterPage(cls.driver,cls.url)
        LoginAction.login_action(cls.zixunapp_page)
        time.sleep(3)
        cls.zixunapp_page.go_appcenter()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_addApp(self):
        '''正流程:添加咨询类app应用'''
        data=self.get_xml.make_child_data('AppCenterPage/zixun_app')
        self.log=Logger()
        self.log.info(u'126邮箱应用中心app测试')
        self.log.info('=========================')
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.zixunapp_page.changeIframe(data['iframe'])
        # 打开咨询分类应用并添加app
        self.zixunapp_page.js_focus_element(self.zixunapp_page.zixun_loc)
        self.zixunapp_page.clickZiXun()
        time.sleep(3)
        self.zixunapp_page.clickApp(self.zixunapp_page.wangyiyun_loc)
        # 返回主页面
        self.zixunapp_page.changeIframeOut()

        # 确认提示框
        self.zixunapp_page.clickAddApp()
        time.sleep(3)
        try:
            self.zixunapp_page.assert_text_in_element(self.zixunapp_page.tip_sucess_loc, data['assert1'])
            self.log.info(u"【%s】应用添加成功" % data['appname'])
        except Exception:
            self.log.error(u"【%s】应用添加失败" % data['appname'])
            self.zixunapp_page.getImageFile('添加应用%s'% data['appname'])
            raise

        # 打开app并校验标题
        try:
            self.zixunapp_page.clickSubmitButton()
            time.sleep(3)
            self.log.info(u"【%s】应用打开成功" % data['appname'])
        except Exception:
            self.log.error(u"【%s】应用打开失败" % data['appname'])
            self.zixunapp_page.getImageFile('打开应用%s'% data['appname'])
            raise

    def test_delApp(self):
        '''正流程:删除咨询类app应用'''
        data = self.get_xml.make_child_data('AppCenterPage/zixun_app')
        self.log = Logger()
        self.zixunapp_page.go_appcenter()
        # 切换iframe
        time.sleep(2)
        self.zixunapp_page.changeIframe(data['iframe'])
        self.zixunapp_page.js_focus_element(self.zixunapp_page.my_application_loc)
        self.zixunapp_page.click_shouyetuijian()
        time.sleep(1)
        self.zixunapp_page.click_my_app_button()
        time.sleep(3)
        self.zixunapp_page.clickGuanLi()
        self.zixunapp_page.deleteApp()
        self.zixunapp_page.clickBaoCun()
        try:
            self.zixunapp_page.assert_text_in_element(self.zixunapp_page.tip_noapp_loc, data['assert2'])
            self.log.info(u"【%s】应用删除成功"%data['appname'])
            self.log.info(u'执行成功')
            self.log.info('=========================')
        except Exception:
            self.log.error(u"【%s】应用删除失败"%data['appname'])
            self.log.info(u'执行失败')
            self.log.info('=========================')
            self.zixunapp_page.getImageFile(data['description'])
            raise

if __name__=="__main__":
    unittest.main()