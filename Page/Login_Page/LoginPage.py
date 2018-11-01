#!/user/bin/env python
#!encoding=utf-8
from Page.BasePage import BasePage
from selenium.webdriver.common.by import By
'''126邮箱登录页面'''
class LoginPage(BasePage):
    '''============定位器============'''
    username_loc=(By.NAME,'email')
    password_loc=(By.NAME,'password')
    sumbit_loc=(By.ID,'dologin')
    turnright_button_loc=(By.ID,'nextTheme')
    turnleft_button_loc=(By.ID,'prevTheme')
    user_loc = (By.ID, 'spnUid')


    '''============Action============'''
    #打开页面
    def open(self):
        self._open(self.url)

    #输入账号(先清理再输入)
    def inputUsername(self,username):
        self.elementClick(self.username_loc)
        self.elementClear(self.username_loc)
        self.elementInput(self.username_loc,username)

    #输入密码
    def inputPassword(self,password):
        self.elementClick(self.password_loc)
        self.elementInput(self.password_loc,password)

    #提交登录
    def submit(self):
        self.elementClick(self.sumbit_loc)

    #主题后翻
    def clickNextTheme(self):
        self.elementClick(self.turnright_button_loc)

    #主题前翻
    def clickPrevTheme(self):
        self.elementClick(self.turnleft_button_loc)

    #获取报错信息
    def get_error(self):
        error_info=super(LoginPage,self).js_element_loc_text('nerror')
        return error_info