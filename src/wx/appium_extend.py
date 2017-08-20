# coding:utf-8
'''
Created on 2017年8月16日

@author: Administrator
'''
import os
import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from mylog import Logger

class AppiumExtend():

    def __init__(self, driver,log):
        self._driver = driver
        self.log = Logger(log)

    def find_element(self,value,timeout=10,obj=''):
        '''
        :param value: xpath value
        :param timeout: wait for element present seconds
        :param obj: web_element object
        :return: web_element
        '''
        i = 0
        while i < timeout:
            try:
                if not obj:
                    self.log.debug('finding element:{0}'.format(value))
                    return self._driver.find_element(By.XPATH,value)
                else:
                    self.log.debug('finding element:{0}'.format(value))
                    return obj.find_element(By.XPATH,value)
            except NoSuchElementException, ns:
                i += 1
                time.sleep(1)
        self.log.warn('appium can not find element:{0}'.format(value))
        return None

    def find_elements(self,value,timeout=10,obj=''):
        '''
        :param value: xpath value
        :param timeout: wait for elements present seconds
        :param obj: web_elements object
        :return: web_elements
        '''
        i = 0
        while i < timeout:
            try:
                if not obj:
                    self.log.debug('finding elements:{0}'.format(value))
                    return self._driver.find_elements(By.XPATH,value)
                else:
                    self.log.debug('finding elements:{0}'.format(value))
                    return obj.find_elements(By.XPATH,value)
            except NoSuchElementException, ns:
                i += 1
                time.sleep(1)
        self.log.warn('appium can not find elements:{0}'.format(value))
        return None

    def long_press_screen(self,x=100,y=100,duration=2000):
        time.sleep(2)
        self.log.debug('appium try to press screen for {0} seconds'.format(duration))
        os.system('adb shell input swipe {0} {1} 100 100 {2}'.format(x,y,duration))

class xpath():

    def __init__(self,e='/'):
        self.e = e

    def Attribute(self,attr,index=0):
        e = ''
        if not index:
            e += '/*[@{0}]'.format(attr)
        else:
            e += '/*[@{0}][{1}]'.format(attr,index)
        self.e += e
        return xpath(self.e)

    def FrameLayout(self,index=0,attr=''):
        e = '/android.widget.FrameLayout'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return xpath(self.e)

    def LinearLayout(self,index=0,attr=''):
        e = '/android.widget.LinearLayout'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return xpath(self.e)

    def ListView(self,index=0,attr=''):
        e = '/android.widget.ListView'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return xpath(self.e)

    def RelativeLayout(self,index=0,attr=''):
        e = '/android.widget.RelativeLayout'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return xpath(self.e)

    def ViewGroup(self,index=0,attr=''):
        e = '/android.view.ViewGroup'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return xpath(self.e)

    def TextView(self,index=0,attr=''):
        e = '/android.widget.TextView'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return xpath(self.e)

    def ImageView(self,index=0,attr=''):
        e = '/android.widget.ImageView'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return xpath(self.e)

    def EditText(self,index=0,attr=''):
        e = '/android.widget.EditText'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return xpath(self.e)

    def FrameLayout(self,index=0,attr=''):
        e = '/android.widget.FrameLayout'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return xpath(self.e)

    @property
    def draw(self):
        return self.e
