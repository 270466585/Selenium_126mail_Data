#!/user/bin/env python
#!encoding=utf-8
import unittest
from Common.RunTools import RunTools
from TestCases.Login_Cases.test_Login import LoginTest
from TestCases.SendEmail_Cases.test_SendEmail import SendEmailTest
from TestCases.HongQiEmail_Cases.test_HongQiEmail import HongQiTest
from TestCases.DaiBanEmail_Cases.test_DaiBanEmail import DaiBanTest
from TestCases.TongXun_Cases.test_TongXun import TongXunTest
from TestCases.AppCenter_Cases.test_XiaoLvApp import XiaoLvAppTest
from TestCases.AppCenter_Cases.test_GongJuApp import GongJuAppTest
from TestCases.AppCenter_Cases.test_GouTongApp import GouTongAppTest
from TestCases.AppCenter_Cases.test_ZiXunApp import ZiXunAppTest
from TestCases.AppCenter_Cases.test_YuLeApp import YuLeAppTest
from TestCases.AppCenter_Cases.test_FenXiangApp import FenXiangAppTest
'''用例管理、执行测试、发送邮件'''

#创建一个suite容器，用于加载用例
suite=unittest.TestSuite()

#加载测试用例
suite.addTest(unittest.makeSuite(LoginTest))
suite.addTest(unittest.makeSuite(SendEmailTest))
suite.addTest(unittest.makeSuite(HongQiTest))
suite.addTest(unittest.makeSuite(TongXunTest))
suite.addTest(unittest.makeSuite(DaiBanTest))
suite.addTest(unittest.makeSuite(XiaoLvAppTest))
suite.addTest(unittest.makeSuite(GongJuAppTest))
suite.addTest(unittest.makeSuite(GouTongAppTest))
suite.addTest(unittest.makeSuite(ZiXunAppTest))
suite.addTest(unittest.makeSuite(YuLeAppTest))
suite.addTest(unittest.makeSuite(FenXiangAppTest))


#生成测试报告
runner=RunTools()
runner.createReport(u'126邮箱自动化测试报告',u'126邮箱自动化测试报告',suite)

#获取到最新的测试报告
getfile=runner.findLastReport()

#发送测试报告到指定邮箱（xml默认配置）
runner.sendMail('126邮箱自动化测试报告-罗泽霖',getfile)
runner.sendMailWithFile('126邮箱自动化测试报告-罗泽霖',getfile)
