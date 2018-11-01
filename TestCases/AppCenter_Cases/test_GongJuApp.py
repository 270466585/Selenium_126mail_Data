#!/user/bin/env python
#!encoding=utf-8
import time
import unittest
from Common.XmlTools import XmlTools
from Common.LogTools import Logger
from Page.BasePage import setBrowser
from Common import LoginAction
from Page.AppCenter_Page.AppCenterPage import AppCenterPage

'''126邮箱应用中心工具类app测试'''

class GongJuAppTest(unittest.TestCase):
    '''126邮箱应用中心app测试'''
    @classmethod
    def setUpClass(cls):
        cls.get_xml=XmlTools()
        cls.driver=setBrowser(cls.get_xml.get_node_text('Common/browser'))
        cls.url=LoginAction.seturl
        cls.gongjuapp_page=AppCenterPage(cls.driver,cls.url)
        LoginAction.login_action(cls.gongjuapp_page)
        time.sleep(3)
        cls.gongjuapp_page.go_appcenter()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_addApp(self):
        '''正流程:添加工具类app应用'''
        data=self.get_xml.make_child_data('AppCenterPage/gongju_app')
        self.log=Logger()
        self.log.info(u'126邮箱应用中心app测试')
        self.log.info('=========================')
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.gongjuapp_page.changeIframe(data['iframe'])
        # 打开工具分类应用并添加app
        self.gongjuapp_page.js_focus_element(self.gongjuapp_page.gongju_loc)
        self.gongjuapp_page.clickGongJu()
        time.sleep(3)
        self.gongjuapp_page.clickApp(self.gongjuapp_page.wangyi_money_loc)
        # 返回主页面
        self.gongjuapp_page.changeIframeOut()

        # 确认提示框
        self.gongjuapp_page.clickAddApp()
        time.sleep(3)
        try:
            self.gongjuapp_page.assert_text_in_element(self.gongjuapp_page.tip_sucess_loc, data['assert1'])
            self.log.info(u"【%s】应用添加成功" % data['appname'])
        except Exception:
            self.log.error(u"【%s】应用添加失败" % data['appname'])
            self.gongjuapp_page.getImageFile('添加应用%s'% data['appname'])
            raise

        # 打开app并校验标题
        try:
            self.gongjuapp_page.clickSubmitButton()
            time.sleep(3)
            self.log.info(u"【%s】应用打开成功" % data['appname'])
        except Exception:
            self.log.error(u"【%s】应用打开失败" % data['appname'])
            self.gongjuapp_page.getImageFile('打开应用%s'% data['appname'])
            raise

    def test_delApp(self):
        '''正流程:删除工具类app应用'''
        data = self.get_xml.make_child_data('AppCenterPage/gongju_app')
        self.log = Logger()
        self.gongjuapp_page.go_appcenter()
        # 切换iframe
        time.sleep(2)
        self.gongjuapp_page.changeIframe(data['iframe'])
        self.gongjuapp_page.js_focus_element(self.gongjuapp_page.my_application_loc)
        self.gongjuapp_page.click_shouyetuijian()
        time.sleep(1)
        self.gongjuapp_page.click_my_app_button()
        time.sleep(3)
        self.gongjuapp_page.clickGuanLi()
        self.gongjuapp_page.deleteApp()
        self.gongjuapp_page.clickBaoCun()
        try:
            self.gongjuapp_page.assert_text_in_element(self.gongjuapp_page.tip_noapp_loc, data['assert2'])
            self.log.info(u"【%s】应用删除成功"%data['appname'])
            self.log.info(u'执行成功')
            self.log.info('=========================')
        except Exception:
            self.log.error(u"【%s】应用删除失败"%data['appname'])
            self.log.info(u'执行失败')
            self.log.info('=========================')
            self.gongjuapp_page.getImageFile(data['description'])
            raise

if __name__=="__main__":
    unittest.main()