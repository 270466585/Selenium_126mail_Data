#!/user/bin/env python
#!encoding=utf-8
import os
import time
import unittest
import smtplib
from Common import PathTools
import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from Common.XmlTools import XmlTools
'''发送邮件'''

'''获取xml文件中email相关数据'''
get_xml=XmlTools()
email_data=get_xml.make_child_data('Common/email')

class RunTools:
    def now(self):
        '''
        获取当前时间
        :return: 返回指定格式的时间
        '''
        self.now=time.strftime("%Y-%m-%d-%H-%M-%S")
        return self.now

    def chooseCase(self,case_path,pattern):
        '''
        选择用例路径下指定测试案例
        :param case_path: 测试用例的目录
        :param pattern: 测试用例文件名匹配模式
        :return: 加载指定测试用例的集合
        '''
        self.discover=unittest.defaultTestLoader.discover(case_path,pattern=pattern)
        return self.discover

    def createReport(self,title,desc,suite):
        '''
        执行用例并生成测试报告
        :param title: 测试报告标题
        :param desc: 测试报告介绍
        :param suite: 测试用例装载容器
        '''
        reportname=PathTools.report_path+"report%s.html"%time.strftime("%Y-%m-%d-%H-%M-%S")
        fp=open(reportname,"wb")
        runner=HTMLTestRunner.HTMLTestRunner(fp,title=title,description=desc)
        runner.run(suite)
        fp.close()

    def findLastReport(self):
        '''
        寻找最新的报告
        :return: 返回最新报告的路径
        '''
        reportlist=os.listdir(PathTools.report_path)
        self.lastreport=reportlist[-1]
        lastreport_path=PathTools.report_path+self.lastreport
        return lastreport_path

    def sendMail(self,subject,sendreport):
        '''
        发送文本内容的邮件
        :param subject:邮件主题
        :param sendreport: 邮件发送报告
        '''
        # 打印附件获取附件内容
        fp = open(sendreport, "rb")
        mail_body = fp.read()
        fp.close()

        # 指定发送方和接收方
        sender = email_data['email_sender']
        receiver = email_data['email_receiver']

        # 配置参数
        msg = MIMEText(mail_body, 'html', 'utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = receiver

        # 发送邮件
        smtp = smtplib.SMTP()
        smtp.connect(email_data['smtp_connect'])
        smtp.login(email_data['smtp_username'], email_data['smtp_password'])
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()

    def sendMailWithFile(self,subject,sendreport):
        '''
        发送邮件并添加附件
        :param subject:邮件主题
        :param sendreport: 邮件发送的报告
        '''
        # 指定发送方和接收方
        sender = email_data['email_sender']
        receiver = email_data['email_receiver']

        #读取文件
        sendfile=open(sendreport,"rb")
        sendfile_read=sendfile.read()
        sendfile.close()

        # 加载邮件附件
        att = MIMEText(sendfile_read, 'base64', 'utf-8')
        att["Content-Type"] = 'application/octet-stream'
        att["Content-Disposition"] = 'attachment;filename=%s' %self.lastreport

        # 配置邮件信息
        msgRoot = MIMEMultipart('related')
        msgRoot['Subject'] = Header(subject, "utf-8")
        msgRoot['From'] = sender
        msgRoot['To'] = receiver
        msgRoot.attach(att)

        #发送邮件
        smtp=smtplib.SMTP()
        smtp.connect(email_data['smtp_connect'])
        smtp.login(email_data['smtp_username'], email_data['smtp_password'])
        smtp.sendmail(sender,receiver,msgRoot.as_string())
        smtp.quit()

