#!/user/bin/env python
#!encoding=utf-8
import random
from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
'''红旗邮件页面'''

class HongQiEmailPage(BasePage):
    '''================定位器================'''
    tip_loc=(By.CSS_SELECTOR,'.rm1')
    qitaqizhi_loc=(By.XPATH,'//div[6]/div/div/div[2]/a')
    qizhi_color_loc=(By.CLASS_NAME,'nui-menu-item-link')
    hongqi_loc=(By.XPATH,'//div[2]/ul/li[2]/div')

    '''================Action================'''

    #进入红旗邮件
    def go_hongqi(self):
        self.elementClick(self.hongqi_loc)

    #点击其他旗帜button
    def click_qita_button(self):
        self.elementClick(self.qitaqizhi_loc)

    #随机选择其中一个旗帜颜色
    def random_qizhi_color(self):
        elements=self.find_elements(self.qizhi_color_loc)
        i=random.randint(0,len(elements)-1)
        return elements[i]

    #点击旗帜颜色并获取颜色
    def click_qizhi_color(self):
        element=self.random_qizhi_color()
        element.click()
        return element.text
