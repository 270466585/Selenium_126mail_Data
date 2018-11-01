#!/user/bin/env python
#!encoding=utf-8
from Page.BasePage import BasePage
from selenium.webdriver.common.by import By

'''应用中心'''

class AppCenterPage(BasePage):
    '''================定位器================'''

    #应用中心
    app_center_loc=(By.XPATH,'//li[4]/a')

    #左边选择框元素定位
    jingpin_loc=(By.XPATH,'//h2')
    all_application_loc=(By.CLASS_NAME,'frame-nav-item.frame-nav-item-hover')
    my_application_loc=(By.XPATH,'//li')
    shouyetuijian_loc=(By.XPATH,"//div[@id='main-nav']/ul/li[3]")

    #应用分类
    xiaolv_loc=(By.XPATH,'//li[9]')
    gongju_loc=(By.XPATH,'//li[10]')
    goutong_loc=(By.XPATH,'//li[11]')
    zixun_loc=(By.XPATH,'//li[12]')
    yule_loc=(By.XPATH,'//li[13]')
    fenxiang_loc=(By.XPATH,'//li[14]')
    youxi_loc=(By.XPATH,'//li[15]')
    wanggou_loc=(By.XPATH,'//li[16]')

    #每个应用分类选取一个应用
    #效率类应用
    VIPmail_loc=(By.XPATH,"//img[@alt='VIP邮箱']")
    #工具类应用
    wangyi_money_loc=(By.XPATH,"//img[@alt='网易有钱']")
    #沟通类应用
    youxianghuangye_loc=(By.XPATH,"//img[@alt='邮箱黄页']")
    #资讯类应用
    wangyiyun_loc=(By.XPATH,"//img[@alt='网易云课堂']")
    #娱乐类应用
    wangyicc_loc=(By.XPATH,"//img[@alt='网易CC']")
    #分享类应用
    wangyiboke_loc=(By.XPATH,"//img[@alt='网易博客']")
    #游戏类应用
    tuomasi_loc=(By.XPATH,"//img[@alt='托马斯小游戏']")
    #网购类应用
    wangyikaola_loc=(By.XPATH,"//img[@alt='网易考拉海购']")


    table_name_loc=(By.XPATH,'//div/div[2]/div/div/h2')
    tianjia_button_loc=(By.XPATH,"//div[2]/div/div/div[2]/a")
    tip_sucess_loc=(By.XPATH,'//div[6]/div[2]/div/div/div')
    tryapp_loc=(By.XPATH,"//div[2]/div/div/div[2]/a[2]")
    useapp_loc=(By.XPATH,'//div[3]/div[2]/div/span')

    #应用管理
    guanli_button_loc=(By.XPATH,"//a[contains(text(),'管理')]")
    delete_app_button_loc=(By.XPATH,'//li/a')
    baocun_button_loc=(By.XPATH,"//a[contains(text(),'保存')]")
    tip_noapp_loc=(By.XPATH,'//p')

    #其他
    myapp_loc=(By.XPATH,'//header/div/a')
    shouye_loc=(By.XPATH,'//div[3]')
    '''================Action================'''

    #进入应用中心
    def go_appcenter(self):
        self.elementClick(self.app_center_loc)

    #点击我的应用
    def clickMyApp(self):
        self.elementClick(self.my_application_loc)

    #点击效率分类应用
    def clickXiaoLv(self):
        self.elementClick(self.xiaolv_loc)

    #点击工具分类应用
    def clickGongJu(self):
        self.elementClick(self.gongju_loc)

    #点击沟通分类应用
    def clickGouTong(self):
        self.elementClick(self.goutong_loc)

    #点击咨询分类应用
    def clickZiXun(self):
        self.elementClick(self.zixun_loc)

    #点击娱乐分类应用
    def clickYuLe(self):
        self.elementClick(self.yule_loc)

    #点击分享分类应用
    def clickFenXiang(self):
        self.elementClick(self.fenxiang_loc)

    #点击游戏分类应用
    def clickYouXi(self):
        self.elementClick(self.youxi_loc)

    #点击网购分类应用
    def clickWangGou(self):
        self.elementClick(self.wanggou_loc)

    #点击某个应用
    def clickApp(self,loc):
        self.elementClick(loc)

    #添加到我的应用
    def clickAddApp(self):
        self.elementClick(self.tianjia_button_loc)

    #点击立即使用
    def clickSubmitButton(self):
        self.elementClick(self.useapp_loc)

    #关闭窗口
    def closeWin(self):
        self.closeDriver()

    #点击管理
    def clickGuanLi(self):
        self.elementClick(self.guanli_button_loc)

    #点击保存
    def clickBaoCun(self):
        self.elementClick(self.baocun_button_loc)

    #删除app
    def deleteApp(self):
        self.elementClick(self.delete_app_button_loc)

    #获取app的名称
    def getAppName(self,loc):
        element=self.find_element(loc)
        return element.text

    #返回首页
    def back_to_shouye(self):
        self.elementClick(self.shouye_loc)

    #点击首页推荐中的“我的应用”
    def click_my_app_button(self):
        self.elementClick(self.myapp_loc)

    #点击首页推荐
    def click_shouyetuijian(self):
        self.elementClick(self.shouyetuijian_loc)