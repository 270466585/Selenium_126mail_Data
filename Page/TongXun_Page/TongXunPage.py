#!/user/bin/env python
#!encoding=utf-8
from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
'''通讯录模块'''

class TongXunPage(BasePage):
    '''================定位器================'''

    tongxun_mokuai_loc = (By.XPATH, '//li[2]/div[3]')
    tongbu_loc=(By.XPATH,'//div[4]/div/a')
    create_lianxiren_loc=(By.XPATH,'//section[2]/div/div/span')
    detele_lianxiren_loc=(By.XPATH,'//header/div/div[2]/div[3]/span')
    all_choose_loc=(By.XPATH,'//th[2]/span/span/b')


    #创建联系人弹出框元素
    table_name_loc=(By.CLASS_NAME,'nui-msgbox-hd')
    name_loc=(By.ID,'input_N')
    email_adr_loc=(By.XPATH,"//div[2]/div/div/div/div/div/div/dl/dd/div/input")
    tel_loc = (By.XPATH, "(//input[@type='text'])[7]")
    beizhu_loc=(By.XPATH,"//dd/div/textarea")
    submit_loc=(By.XPATH,'//div[3]/div[2]/div/span')


    #联系人创建后元素
    email_loc=(By.CSS_SELECTOR,'nobr.de0')

    #删除弹出框
    delete_title_loc=(By.CLASS_NAME,'nui-msgbox-title')
    accept_button_loc=(By.XPATH,'//div[3]/div[2]/div/span')

    #其他
    tip_loc=(By.XPATH,'//p/strong')


    '''================Action================'''

    #打开通讯录
    def go_TongXun(self):
        self.elementClick(self.tongxun_mokuai_loc)

    #创建联系人
    def clickCreatePeople(self):
        self.elementClick(self.create_lianxiren_loc)

    #输入联系人姓名
    def inputCreateName(self,name):
        self.elementClick(self.name_loc)
        self.elementInput(self.name_loc,name)

    #输入联系人email
    def inputEamil(self,email):
        self.elementClick(self.email_adr_loc)
        self.elementInput(self.email_adr_loc,email)

    #输入联系人电话
    def inputTel(self,telnum):
        self.elementClick(self.tel_loc)
        self.elementInput(self.tel_loc,telnum)

    #输入备注信息
    def inputBeiZhu(self,beizhuinfo):
        self.elementClick(self.beizhu_loc)
        self.elementInput(self.beizhu_loc,beizhuinfo)

    #点击确定
    def submit(self):
        self.elementClick(self.submit_loc)

    #全选
    def all_choose(self):
        self.elementClick(self.all_choose_loc)

    #删除联系人
    def deletePeople(self):
        self.elementClick(self.detele_lianxiren_loc)

    #确认删除联系人提示框
    def acceptDelete(self):
        self.elementClick(self.accept_button_loc)

    #获取提示框错误信息
    def get_tip_error(self):
        errorinfo=self.js_elements_loc_text('classname','nui-msgbox-ft-text',0)
        return errorinfo