#!/user/bin/env python
#!encoding=utf-8
import time
import unittest
from Common.XmlTools import XmlTools
from Common.LogTools import Logger
from Page.BasePage import setBrowser
from Common import LoginAction
from Page.AppCenter_Page.AppCenterPage import AppCenterPage

'''126邮箱应用中心娱乐类app测试'''

class YuLeAppTest(unittest.TestCase):
    '''126邮箱应用中心app测试'''
    @classmethod
    def setUpClass(cls):
        cls.get_xml=XmlTools()
        cls.driver=setBrowser(cls.get_xml.get_node_text('Common/browser'))
        cls.url=LoginAction.seturl
        cls.yuleapp_page=AppCenterPage(cls.driver,cls.url)
        LoginAction.login_action(cls.yuleapp_page)
        time.sleep(3)
        cls.yuleapp_page.go_appcenter()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_addApp(self):
        '''正流程:添加娱乐类app应用'''
        data=self.get_xml.make_child_data('AppCenterPage/yule_app')
        self.log=Logger()
        self.log.info(u'126邮箱应用中心app测试')
        self.log.info('=========================')
        self.log.info(data['description'])
        self.log.info(u'执行开始')

        #执行操作
        self.yuleapp_page.changeIframe(data['iframe'])
        # 打开娱乐分类应用并添加app
        self.yuleapp_page.js_focus_element(self.yuleapp_page.yule_loc)
        self.yuleapp_page.clickYuLe()
        time.sleep(3)
        self.yuleapp_page.clickApp(self.yuleapp_page.wangyicc_loc)
        # 返回主页面
        self.yuleapp_page.changeIframeOut()

        # 确认提示框
        self.yuleapp_page.clickAddApp()
        time.sleep(3)
        try:
            self.yuleapp_page.assert_text_in_element(self.yuleapp_page.tip_sucess_loc, data['assert1'])
            self.log.info(u"【%s】应用添加成功" % data['appname'])
        except Exception:
            self.log.error(u"【%s】应用添加失败" % data['appname'])
            self.yuleapp_page.getImageFile('添加应用%s'% data['appname'])
            raise

        # 打开app并校验标题
        try:
            self.yuleapp_page.clickSubmitButton()
            time.sleep(3)
            # 获取所有窗口句柄
            self.handles = self.yuleapp_page.get_all_handles()
            # 跳转至指定句柄
            self.yuleapp_page.change_handle(self.handles, 1)
            self.yuleapp_page.assert_title_contains(data['appname'])
            time.sleep(3)
            self.log.info(u"【%s】应用打开成功" % data['appname'])
            self.yuleapp_page.closeWin()  # 关闭窗口
            self.yuleapp_page.change_handle(self.handles, 0)
        except Exception:
            self.log.error(u"【%s】应用打开失败" % data['appname'])
            self.yuleapp_page.getImageFile('打开应用%s'% data['appname'])
            raise

    def test_delApp(self):
        '''正流程:删除娱乐类app应用'''
        data = self.get_xml.make_child_data('AppCenterPage/yule_app')
        self.log = Logger()
        # 切换iframe
        time.sleep(2)
        self.yuleapp_page.changeIframe(data['iframe'])
        self.yuleapp_page.js_focus_element(self.yuleapp_page.my_application_loc)
        self.yuleapp_page.click_shouyetuijian()
        time.sleep(1)
        self.yuleapp_page.click_my_app_button()
        time.sleep(3)
        self.yuleapp_page.clickGuanLi()
        self.yuleapp_page.deleteApp()
        self.yuleapp_page.clickBaoCun()
        try:
            self.yuleapp_page.assert_text_in_element(self.yuleapp_page.tip_noapp_loc, data['assert2'])
            self.log.info(u"【%s】应用删除成功"%data['appname'])
            self.log.info(u'执行成功')
            self.log.info('=========================')
        except Exception:
            self.log.error(u"【%s】应用删除失败"%data['appname'])
            self.log.info(u'执行失败')
            self.log.info('=========================')
            self.yuleapp_page.getImageFile(data['description'])
            raise

if __name__=="__main__":
    unittest.main()