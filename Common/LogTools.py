#!/user/bin/env python
#!encoding=utf-8
import sys
import time
import logging
from Common.PathTools import log_path

'''日志创建方法封装'''

class Logger:
    def __init__(self):
        '''logger日志创建基础属性'''
        self.logname=log_path+'%s.log'%time.strftime("%Y-%m-%d")
        self.logger=logging.getLogger()
        self.logger.setLevel(logging.DEBUG)
        #设置日志格式
        self.fromatter=logging.Formatter('[%(asctime)s] - [%(levelname)s] - %(message)s')
        #获取当前调用的名称
        self.log_cur_name=str(sys._getframe().f_back.f_code.co_name)

    def _addlog(self,level,message):
        '''
        日志文件创建与输入
        :param level: 日志等级
        :param message: 日志内容
        '''
        # 创建一个FileHandler，用于写到本地
        fh=logging.FileHandler(self.logname,'a',encoding='utf-8')    #追加模式并设置编码为utf-8
        fh.setLevel(logging.INFO)
        fh.setFormatter(self.fromatter)
        self.logger.addHandler(fh)
        # 创建一个StreamHandler,用于输出到控制台
        ch=logging.StreamHandler()
        ch.setLevel(logging.INFO)
        ch.setFormatter(self.fromatter)
        self.logger.addHandler(ch)
        #调用四种不同级别的输入方法
        if level=='info':
            self.logger.info("".join([self.log_cur_name," - run: ",message]))
        elif level=='debug':
            self.logger.debug("".join([self.log_cur_name," - run: ",message]))
        elif level=='warning':
            self.logger.warning("".join([self.log_cur_name," - run: ",message]))
        elif level=='error':
            self.logger.error("".join([self.log_cur_name," - run: ",message]))
        else:
            print ('日志等级选择有误，日志等级为:%s')%level
        #这两行代码是为了避免日志输出重复问题
        self.logger.removeHandler(ch)
        self.logger.removeHandler(fh)
        #关闭打开的文件
        fh.close()

    def info(self,message):
        '''
        日志输入info等级信息
        :param message: info信息
        '''
        self._addlog('info',message)

    def debug(self,message):
        '''
        日志输入debug等级信息
        :param message: debug信息
        '''
        self._addlog('debug',message)

    def warning(self,message):
        '''
        日志输入warning等级信息
        :param message: warning信息
        '''
        self._addlog('warning',message)

    def error(self,message):
        '''
        日志输入error等级信息
        :param message: error信息
        '''
        self._addlog('error',message)

    # 封装一个获取调用函数名的方法，便于将运行case时将case名打印在日志上
    def log_cur_name(self):
        '''
        获取当前调用的函数
        '''
        return str(sys._getframe().f_back.f_code.co_name)

