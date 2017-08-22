# coding:utf-8
'''
Created on 2017年8月16日

@author: Administrator
'''
import unittest
from selenium import webdriver
from business import Wechat

class Test(unittest.TestCase):
    def setUp(self):
        self.desired_caps = {}
        self.desired_caps["platformName"] = "Android"
        self.desired_caps["platformVersion"] = "6.0.1"
        self.desired_caps["deviceName"] = "Redmi Note 4X"
        self.desired_caps["appPackage"] = "com.tencent.mm"
        self.desired_caps["appActivity"] = ".ui.LauncherUI"
        self.desired_caps["noReset"] = True
        self.desired_caps["resetKeyboard"] = True
        self.desired_caps["unicodeKeyboard"] = True
        self.desired_caps["udid"] = "c284c8500903"
        self.desired_caps["clearSystemFiles"] = True
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
        self.driver.implicitly_wait(1)
        self.wechat = Wechat(self.driver,log='info')

    def tearDown(self):
        self.driver.quit()
        print 'done'

    def test_public1(self):
        self.wechat.initial_scenario(code=u'信用卡',public_name='微信公众平台测试号')
        self.wechat.send_msg(u'你好')
        print self.wechat.get_last_agent_msg()
        self.wechat.find_service([u'易 •服务',u'积分查询'])
        print self.wechat.get_last_agent_msg()
        self.wechat.send_msg(u'转人工')
        print self.wechat.get_last_agent_msg()
    #
    # def test_public2(self):
    #     self.wechat.initial_scenario(code=u'银行',public_name='微信公众平台测试号')
    #     self.wechat.send_msg(u'你好')
    #     print self.wechat.get_last_agent_msg()
    #     self.wechat.send_msg(u'转人工')
    #     print self.wechat.get_last_agent_msg()
    #
    #
    # def test_public3(self):
    #     self.wechat.initial_scenario(code=u'信用卡',public_name='微信公众平台测试号')
    #     self.wechat.send_msg(u'你好')
    #     print self.wechat.get_last_agent_msg()
    #     self.wechat.send_msg(u'转人工')
    #     print self.wechat.get_last_agent_msg()

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
