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
from element import element

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
        self._driver_find_element(by=By.XPATH,value="//*[@text='公众号']").click()
        self._driver_find_element(by=By.XPATH,value="//*[@text='统一通讯平台服务号']").click()
        # self._driver_find_element(by=By.XPATH, value="//android.widget.ImageView[@content-desc='消息']").click()
        # self._driver_find_element(by=By.CLASS_NAME,value="android.widget.EditText").send_keys(u'平安银行信用卡')
        # self._driver_find_element(by=By.XPATH,value="//*[@text='发送']").click()
        value = element('/').FrameLayout("content-desc='当前所在页面,与统一通讯平台服务号的聊天'").FrameLayout().LinearLayout(index=2).FrameLayout().FrameLayout().LinearLayout().FrameLayout(index=2).FrameLayout().ListView().draw
        print value
        print self._driver_find_element(by=By.XPATH,value=value)

    def _driver_find_element(self, by, value):
        return self.wait_for_element_present(by,value)

    def _driver_find_elements(self, by, value):
        return self.wait_for_elements_present(by,value)

    def wait_for_element_present(self, by,value, timeout=10):
        i = 0
        while i < timeout:
            try:
                return self.driver.find_element(by,value)
            except NoSuchElementException, ns:
                i += 1
                time.sleep(1)

    def wait_for_elements_present(self, by,value, timeout=10):
        i = 0
        while i < timeout:
            try:
                return self.driver.find_elements(by,value)
            except NoSuchElementException, ns:
                i += 1
                time.sleep(1)

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()