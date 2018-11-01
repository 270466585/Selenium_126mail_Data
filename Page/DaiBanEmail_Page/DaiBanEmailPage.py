#!/user/bin/env python
#!encoding=utf-8
from Page.BasePage import BasePage
from selenium.webdriver.common.by import By

'''待办邮件页面'''

class DaiBanPage(BasePage):
    '''============定位器============'''

    refresh_loc=(By.XPATH,'//div[6]/div/div/div[2]/a')
    daibanyoujian_loc = (By.XPATH, '//div[2]/ul/li[3]/div')

    '''============Action============'''

    #点击待办邮件模块
    def go_daiban(self):
        self.elementClick(self.daibanyoujian_loc)

    #点击“重新刷新试试”
    def clickRefresh(self):
        self.elementClick(self.refresh_loc)

    #获取提示信息
    def get_tip(self):
        text=self.js_elements_loc_text('classname','rm1',0)
        return text

