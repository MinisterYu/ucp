# coding:utf-8
'''
Created on 2017年8月16日

@author: Administrator
'''
import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
from selenium.webdriver.common.by import By
from element import root

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
        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
        self.driver.implicitly_wait(1)

    def tearDown(self):
        self.driver.quit()

    def test_public(self):
        self._driver_find_element(by=By.XPATH,value="//*[@text='通讯录']").click()
        print  self._driver_find_elements(by=By.XPATH,value="//*[@text='公众号']")
        self._driver_find_element(by=By.XPATH, value="//*[@text='公众号']").click()
        self._driver_find_element(by=By.XPATH,value="//*[@text='统一通讯平台服务号']").click()
        # self._driver_find_element(by=By.XPATH, value="//android.widget.ImageView[@content-desc='消息']").click()
        # self._driver_find_element(by=By.CLASS_NAME,value="android.widget.EditText").send_keys(u'平安银行信用卡')
        # self._driver_find_element(by=By.XPATH,value="//*[@text='发送']").click()
        list_view = root().FrameLayout(attr='content-desc="当前所在页面,与统一通讯平台服务号的聊天"')\
            .FrameLayout()\
            .LinearLayout()\
            .FrameLayout()\
            .ViewGroup()\
            .FrameLayout(1)\
            .LinearLayout()\
            .FrameLayout()\
            .LinearLayout()\
            .FrameLayout()\
            .FrameLayout()\
            .ListView().RelativeLayout().draw

        #   LinearLayout().LinearLayout().LinearLayout().TextView().draw
        # print value
        last_msg = self._driver_find_elements(by=By.XPATH,value=list_view)[-1]

        # '//android.widget.LinearLayout/android.widget.RelativeLayout/*[@content-desc='#{agent}']"'
        agent_icon = root().LinearLayout().RelativeLayout().Attribute("content-desc='统一通讯平台服务号头像'").draw
        print agent_icon
        # //android.widget.LinearLayout/android.widget.LinearLayout
        pic = root().LinearLayout().LinearLayout().draw
        self._driver_find_element(by=By.XPATH,value=agent_icon,obj=last_msg)
        self._driver_find_element(by=By.XPATH,value=pic,obj=last_msg).click()


    def _driver_find_element(self, by, value, timeout=10,obj=''):
        return self.wait_for_element_present(by,value,timeout,obj)

    def _driver_find_elements(self, by, value):
        return self.wait_for_elements_present(by,value)

    def wait_for_element_present(self, by,value,timeout,obj):
        i = 0
        while i < timeout:
            try:
                if not obj:
                    return self.driver.find_element(by,value)
                else:
                    return obj.find_element(by,value)
            except NoSuchElementException, ns:
                i += 1
                time.sleep(1)
        raise Exception()

    def wait_for_elements_present(self, by,value, timeout=10):
        i = 0
        while i < timeout:
            try:
                return self.driver.find_elements(by,value)
            except NoSuchElementException, ns:
                i += 1
                time.sleep(1)
        raise Exception()

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
