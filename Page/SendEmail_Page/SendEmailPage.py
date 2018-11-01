#!/user/bin/env python
#!encoding=utf-8
from Page.BasePage import BasePage
from selenium.webdriver.common.by import By

'''写信发送邮件界面'''

class SendEmailPage(BasePage):
    '''================定位器================'''

    #写信按键
    xiexin_loc = (By.CSS_SELECTOR, '.oz0')

    # 按钮组
    button_loc = (By.CLASS_NAME, 'nui-toolbar-item')
    fasong_button_loc=(By.XPATH,'//footer/div/span[2]')

    #写信要素
    #收件人信息
    shoujianren_loc1 = (By.CLASS_NAME, 'js-component-emailtips')
    shoujianren_loc2 = (By.CLASS_NAME, 'nui-editableAddr-ipt')

    #主题信息
    subject_loc=(By.XPATH,'//header/div[2]/div/div/div/input')

    #文本编辑框
    edit_body_loc = (By.XPATH, 'html/body')

    #iframe切换定位
    iframe_loc = (By.CLASS_NAME, 'APP-editor-iframe')

    #报错定位
    error_loc=(By.XPATH,'//body/div[7]')

    #其他
    upload_button_loc = (By.LINK_TEXT, u'从手机上传图片')
    continue_sendemail_loc=(By.XPATH,'//section/div[3]/a[3]')

    #提示框
    tip_loc=(By.CSS_SELECTOR,'.nui-msgbox-title')
    queding_button_loc=(By.XPATH,'//div[3]/div[2]/div/span')
    quxiao_button_loc=(By.XPATH,'//div[3]/div[2]/div[2]/span')

    '''================Action================'''

    # 点击写信
    def go_xiexin(self):
        elements=self.find_elements(self.xiexin_loc)
        elements[1].click()

    # 点击发送按钮
    def clickFaSongButton(self):
        element=self.find_elements(self.button_loc)[0]
        element.click()

    # 点击预览按钮
    def clickYuLanButton(self):
        element = self.find_elements(self.button_loc)[1]
        element.click()

    # 点击存草稿按钮
    def clickCaoGaoButton(self):
        element = self.find_elements(self.button_loc)[2]
        element.click()

    # 点击取消按钮
    def clickQuXiaoButton(self):
        element = self.find_elements(self.button_loc)[3]
        element.click()

    #点击收件人并输入收件人信息
    def inputShouJianInfo(self,email_path):
        self.elementClick(self.shoujianren_loc1)
        self.elementInput(self.shoujianren_loc2,email_path)

    #点击主题并输入主题信息
    def inputSubject(self,subject):
        self.elementClick(self.subject_loc)
        self.elementInput(self.subject_loc,subject)

    #文本编辑
    def editText(self,email_text):
        self.elementClick(self.edit_body_loc)
        self.elementInput(self.edit_body_loc,email_text)

    #获取报错
    def get_error(self):
        error_info=self.js_elements_loc_text('classname','nui-tips-text',0)
        return error_info

    #点击确定按钮
    def click_queding_button(self):
        self.elementClick(self.queding_button_loc)

    #点击取消按钮
    def click_quxiao_button(self):
        self.elementClick(self.quxiao_button_loc)
