#!/user/bin/env python
#!encoding=utf-8
import time
from Common.PathTools import *
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC

'''封装页面公用方法'''

#封装浏览器
def setBrowser(browserinfo):
    '''
    设置浏览器
    :param browserinfo:输入浏览器信息（firefox、chrome、ie）
    :return:对应浏览器的驱动
    '''
    if browserinfo=='friefox':
        browser=webdriver.Firefox()
        return browser
    if browserinfo=='chrome':
        browser=webdriver.Chrome('C:\\Users\\Administrator\\AppData\\Local\\Google\\chromedriver.exe')
        return browser
    if browserinfo=='ie':
        browser=webdriver.Ie()
        return browser

class BasePage(object):
    def __init__(self,selenium_driver,base_url):
        '''
        初始化
        :param selenium_driver:driver驱动
        :param base_url: 需要打开的url
        '''
        self.driver=selenium_driver
        self.url=base_url

    def now(self):
        '''
        获取当前时间
        :return: 当前时间
        '''
        self.now=time.strftime("%Y-%m-%d-%H-%M-%S")
        return self.now

    def _open(self,url):
        '''
        打开url
        :param url:需要打开的url地址
        '''
        self.driver.get(url)

    '''=============元素定位============='''

    def find_element(self,loc):
        '''
        重写find_element方法，增加定位元素的健壮性
        :param loc: 元素定位loc
        :return: 定位元素
        '''
        try:
            element=WebDriverWait(self.driver,10).until(EC.presence_of_element_located(loc))
            return element
        except:
            print("Can't find the element:%s"%str(loc))

    def find_elements(self,loc):
        '''
        重写find_elements方法，增加定位元素的健壮性
        :param loc: 元素定位loc
        :return: 定位元素，是一个列表保存多个元素定位
        '''
        try:
            elements=WebDriverWait(self.driver,10).until(EC.presence_of_all_elements_located(loc))
            return elements
        except:
            print("Can't find the elements:%s"%str(loc))

    def xpath_element_with_text(self,text):
        '''
        xpath模糊定位,通过文本内容定位
        :param text: 文本信息
        :return: 定位元素
        '''
        element=self.driver.find_element_by_xpath("//*[contains(text(),%s)]"%text)
        return element

    def xpath_element_with_attribute(self,attribute,value):
        '''
        xpath模糊定位，通过匹配属性定位
        :param attribute: 元素属性
        :param value: 元素的value值
        :return: 定位元素
        '''
        element=self.driver.find_element_by_xpath("//*[contains(@%s,%s)]"%(attribute,value))
        return element

    def xpath_element_startwith(self,attribute,value):
        '''
        xpath模拟定位，通过匹配属性开头信息
        :param attribute:元素属性
        :param value: 元素属性的开头value
        :return:定位元素
        '''
        element=self.driver.find_element_by_xpath("//*[starts-with(@%s,%s)]"%(attribute,value))
        return element

    def xpath_element_endwith(self,attribute,value):
        '''
        xpath模拟定位，通过匹配属性结尾信息
        :param attribute: 元素属性
        :param value: 元素属性的结尾value
        :return: 定位元素
        '''
        element=self.driver.find_element_by_xpath("//*[ends-with(@%s,%s)]"%(attribute,value))
        return element

    def xpath_element_with_re(self,text):
        '''
        xpath支持正则表达式匹配
        :param text: 正则匹配文本
        :return: 定位元素
        '''
        element=self.driver.find_element_by_xpath("//*[matchs(text(),%s)]"%text)
        return element

    def xpath_element_with_tagname(self,tagname,attribute,value):
        '''
        xpath通过tagname标签进一步定位元素
        :param tagname: 标签信息
        :param attribute: 属性内容
        :param value: 元素value
        :return: 定位元素
        '''
        element=self.driver.find_element_by_xpath("//%s[contains(@%s,%s)]"%(tagname,attribute,value))
        return element

    '''=============页面操作============='''
    def maximize(self):
        '''
        浏览器最大化
        '''
        self.driver.maximize_window()

    def elementClick(self,loc):
        '''
        元素点击
        :param loc:元素定位
        :return: 元素定位后执行点击
        '''
        element=self.find_element(loc)
        element.click()


    def elementClear(self,loc):
        '''
        元素清空
        :param loc:元素定位
        :return: 元素定位后执行清空
        '''
        element=self.find_element(loc)
        element.clear()


    def elementInput(self,loc,value):
        '''
        元素输入信息
        :param loc:元素定位
        :param value: 输入的信息
        :return: 元素定位后执行输入操作
        '''
        element=self.find_element(loc)
        element.send_keys(value)

    def elementsClick(self,loc,index):
        '''
        指定元素集合中某个元素点击,index=0为第一个
        :param loc: 元素定位，获取元素列表
        :param index: 元素定位index
        :return: 指定某一个元素后执行点击操作
        '''
        elements=self.find_elements(loc)
        elements[index].click()

    def elementsClear(self,loc,index):
        '''
        指定元素集合中某个元素清空输入域,index=0为第一个
        :param loc: 元素定位，获取元素列表
        :param index: 元素定位index
        :return: 指定某一个元素后执行清空操作
        '''
        elements=self.find_elements(loc)
        elements[index].clear()

    def elementsInput(self,loc,index,value):
        '''
        指定元素集合中某个元素输入value,index=0为第一个
        :param loc: 元素定位，获取元素列表
        :param index: 元素定位index
        :param value: 输入的value值
        :return: 指定某一个元素后执行输入value值
        '''
        elements=self.find_elements(loc)
        elements[index].send_keys(value)

    def changeIframe(self,iframe):
        '''
        切换iframe
        :param iframe:指定切换的iframe
        '''
        self.driver.switch_to_frame(iframe)

    def changeIframe_index(self,index):
        '''
        通过iframe所在的index切换iframe
        :param index:iframe所在的index
        '''
        self.driver.switch_to_frame(index)

    def changeIframe_element(self,loc):
        '''
        通过元素定位切换iframe
        :param loc: 元素定位
        '''
        element=self.find_element(loc)
        self.driver.switch_to_frame(element)

    def changeIframeOut(self):
        '''
        从iframe切换出主页
        '''
        self.driver.switch_to_default_content()

    def forward(self):
        '''
        网页前进
        '''
        self.driver.forward()

    def back(self):
        '''
        网页后退
        '''
        self.driver.back()

    def closeDriver(self):
        '''
        关闭窗口
        '''
        self.driver.close()

    def quitDriver(self):
        '''
        退出全部窗口
        '''
        self.driver.quit()

    def getImageFile(self,image_name):
        '''
        截图保存
        :param image_name:截图文件名称
        :return: 指定目录中保存截图文件
        '''
        imagefile=image_path+time.strftime("%Y-%m-%d-%H-%M-%S")+"_"+image_name+".jpg"
        try:
            self.driver.get_screenshot_as_file(imagefile)
        except:
            print("截图失败,文件名为%s:"%image_name)

    '''=============断言方法============='''

    def assert_equal(self,param1,param2):
        '''
        判断两个参数值是否一致
        :param param1:参数值
        :param param2:参数值
        :return:True或者False
        '''
        if param1==param2:
            return True
        else:
            return False

    def assert_title_is(self,except_title,timeout=10):
        '''
        判断标题是否为预期结果
        :param except_title:期望标题
        :param timeout: 超时时间
        :return: 返回True或者False
        '''
        WebDriverWait(self.driver,timeout,1).until(EC.title_is(except_title))

    def assert_title_contains(self,except_title,timeout=10):
        '''
        判断标题是否包含预期字符
        :param except_title:期望标题
        :param timeout: 超时时间
        :return: 返回True或者False
        '''
        WebDriverWait(self.driver,timeout,1).until(EC.title_contains(except_title))

    def assert_text_in_element(self,locator,text,timeout=10):
        '''
        判断定位元素文本是否为预期结果
        :param locator: 元素定位
        :param text: 判断文本
        :param timeout: 超时时间
        :return: 返回True或者False
        '''
        WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element(locator,text))

    def assert_text_in_element_value(self,locator,value,timeout=10):
        '''
        判断定位元素的value值是否为预期结果
        :param locator: 元素定位
        :param value: value的值
        :param timeout: 超时时间
        :return: 返回True或者False
        '''
        WebDriverWait(self.driver,timeout,1).until(EC.text_to_be_present_in_element_value(locator,value))

    def assert_is_selected(self,locator,timeout=10):
        '''
        判断元素是否被选中
        :param locator:元素定位
        :param timeout: 超时时间
        :return: 返回True或者False
        '''
        WebDriverWait(self.driver,timeout,1).until(EC.element_located_to_be_selected(locator))

    def assert_is_selected_be(self, locator, selected=True, timeout=10):
        '''
        判断元素的状态，selected 是期望的参数
        :param locator: 元素定位
        :param selected: 被选中设置为True
        :param timeout: 超时时间
        :return: 返回True或者False
        '''
        WebDriverWait(self.driver,timeout,1).until(EC.element_located_selection_state_to_be(locator,selected))

    def assert_is_alert_present(self, timeout=10):
        '''
        判断是否有alert警告框
        :param timeout: 超时时间
        :return: 返回True或者False
        '''
        WebDriverWait(self.driver,timeout,1).until(EC.alert_is_present())

    def assert_is_visibility(self, locator, timeout=10):
        '''
        判断元素是否可见
        :param locator:元素定位
        :param timeout: 超时时间
        :return: 返回True或者False
        '''
        WebDriverWait(self.driver,timeout,1).until(EC.visibility_of_element_located(locator))

    def assert_is_clickable(self, locator, timeout=10):
        '''
        判断元素是否可以点击
        :param locator: 元素定位
        :param timeout: 超时时间
        :return: 返回True或者False
        '''
        WebDriverWait(self.driver,timeout,1).until(EC.element_to_be_clickable(locator))

    def assert_is_located(self, locator, timeout=10):
        '''
        判断元素是否被定位到
        :param locator: 元素定位
        :param timeout: 超时时间
        :return: 返回True或者False
        '''
        WebDriverWait(self.driver,timeout,1).until(EC.presence_of_element_located(locator))

    '''=============模拟鼠标============='''

    def mouse_to_element(self,locator):
        '''
        模拟鼠标悬停在指定元素上
        :param locator: 元素定位
        :return: 鼠标悬停元素
        '''
        element=self.find_element(locator)
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click_element(self,locator):
        '''
        模拟鼠标双击指定元素
        :param locator: 元素定位
        :return: 鼠标双击元素
        '''
        element = self.find_element(locator)
        ActionChains(self.driver).double_click(element).perform()

    def right_click_element(self,locator):
        '''
        模拟鼠标右击指定元素
        :param locator: 元素定位
        :return: 鼠标右击元素
        '''
        element=self.find_element(locator)
        ActionChains(self.driver).context_click(element).perform()

    '''=============获取各类属性============='''

    def get_title(self):
        '''
        获取标题
        '''
        self.driver.title()

    def get_text(self,locator):
        '''
        获取文本信息
        :param locator:元素定位
        :return: 返回元素的text
        '''
        element=self.find_element(locator)
        element.text()

    def get_attribute(self,locator,name):
        '''
        获取某个元素属性的值
        :param locator: 元素定位
        :param name: 属性
        :return: 返回定位元素属性的值
        '''
        element=self.find_element(locator)
        return element.get_attribute(name)

    def get_current_handle(self):
        '''
        获取当前窗口的句柄
        :return: 返回当前句柄值
        '''
        curhandle=self.driver.current_window_handle
        return curhandle

    def get_all_handles(self):
        '''
        获取所有页面的句柄
        :return: 返回所有句柄值，以列表形式保存
        '''
        allhandles=self.driver.window_handles
        return allhandles

    def change_handle(self,handles,index):
        '''
        切换指定句柄
        :param handles:句柄列表
        :param index: 角标
        :return: 返回指定角标的句柄
        '''
        self.driver.switch_to_window(handles[index])

    '''=============执行JS============='''

    def js_execute(self, js):
        '''
        执行js脚本
        :param js:js语句
        :return: 返回执行js语句
        '''
        return self.driver.execute_script(js)

    def js_focus_element(self, locator):
        '''
        聚焦指定元素
        :param locator:元素定位
        :return: 聚焦到指定的元素
        '''
        target = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView( );", target)

    def js_scroll_top(self):
        '''
        控制竖条滚条拖曳到顶部
        '''
        js="window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self):
        '''
        控制竖条滚条拖曳到底部
        '''
        js="window.scrollTo(0,10000)"
        self.driver.execute_script(js)

    '''=============JS定位============='''

    def js_element_loc(self,locinfo):
        '''利用js定位元素,通过id定位单个元素'''
        js="document.getElementById('%s')"%locinfo
        eleloc=self.js_execute(js)
        return eleloc

    def js_elements_loc(self,locstyle,locinfo):
        '''利用js定位元素，通过name、tagname、classname定位多个元素'''
        if locstyle=='name':  #通过name定位
            js = "document.getElementsByName('%s')" % locinfo
            elesloc = self.js_execute(js)
            return elesloc
        elif locstyle=='tagname':   #通过tagname定位
            js = "document.getElementsByTagName('%s')" % locinfo
            elesloc = self.js_execute(js)
            return elesloc
        elif locstyle=='classname':     #通过classname定位
            js = "document.getElementsByClassName('%s')" % locinfo
            elesloc = self.js_execute(js)
            return elesloc

    def js_element_loc_text(self,locinfo):
        '''获取js定位id元素的文本值'''
        js="document.getElementById('%s').innerHTML"%locinfo
        eleloc_text=self.js_execute(js)
        return eleloc_text

    def js_elements_loc_text(self,locstyle,locinfo,index):
        '''获取js定位复数，通过index获取具体单个元素的文本值'''
        if locstyle=='name':  #通过name定位并获取文本
            js = "document.getElementsByName('%s')[%d].innerHTML" % (locinfo,index)
            eleloc_text = self.js_execute(js)
            return eleloc_text
        elif locstyle=='tagname':   #通过tagname定位并获取文本
            js = "document.getElementsByTagName('%s')[%d].innerHTML" % (locinfo,index)
            eleloc_text = self.js_execute(js)
            return eleloc_text
        elif locstyle=='classname': #通过classname定位并获取文本
            js = "document.getElementsByClassName('%s')[%d].innerHTML" % (locinfo,index)
            eleloc_text = self.js_execute(js)
            return eleloc_text

    '''=============下拉框操作============='''

    def select_by_index(self,locator,index):
        '''
        通过索引，选择指定的选项，从0开始
        :param locator: 元素定位
        :param index: 角标
        :return: 通过index选择下拉框元素
        '''
        element=self.find_element(locator)
        Select(element).select_by_index(index)

    def select_by_value(self,locator,value):
        '''
        通过value值，选择指定的选项
        :param locator: 元素定位
        :param value: value值
        :return:通过value值选择下拉框元素
        '''
        element=self.find_element(locator)
        Select(element).select_by_value(value)

    def select_by_text(self,locator,text):
        '''
        通过文本，选择指定的选项
        :param locator: 元素定位
        :param text: text值
        :return: 通过text值选择下拉框元素
        '''
        element=self.find_element(locator)
        Select(element).select_by_visible_text(text)