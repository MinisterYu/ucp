#coding:utf-8

from selenium.webdriver.common.by import By
from appium_extend import AppiumExtend,xpath
import time
from mylog import Logger

class Wechat():

    def __init__(self,driver,log='debug'):
        self._driver = driver
        self.main_entry = '统一通讯平台服务号'
        self.app = AppiumExtend(self._driver,log)
        self.log = Logger(log)

    def initial_scenario(self,code,public_name='微信公众平台测试号'):
        '''
        初始化测试场景
        :param code: 在统一通讯平台服务号中，输入对应的code，获取公众号二维码信息
        :param public_name: 测试对象的公众号名称，默认验证为“微信公众平台测试号”
        :return: None
        '''
        self.code = code
        self.public_name = public_name
        self.log.info('公众号名称 {0}'.format(code))
        self.app.find_element(xpath().Attribute("text='通讯录'").draw).click()
        self.log.info('点击通讯录')
        self.app.find_element(xpath().Attribute("text='公众号'").draw).click()
        self.log.info('点击公众号选项')
        self.app.find_element(xpath().Attribute("text='{0}'".format(self.main_entry)).draw).click()
        self.log.info('进入【{0}】聊天页面'.format(self.main_entry))
        self.send_msg(self.code)
        self.log.info('发送消息：{0} 给【{1}】'.format(self.code,self.main_entry))
        self.get_last_ucp_image().click()
        self.log.info('点击{0}二维码'.format(code))
        self.app.long_press_screen(duration=2000)
        self.log.info('长按屏幕')
        self.app.find_element(xpath().Attribute("text='识别图中二维码'").draw).click()
        self.log.info('识别图片中的二维码')

    def send_msg(self,keyword):
        '''
        发送文本消息
        :param keyword: 需要发送的文本消息
        :return: None
        '''
        if not self.app.find_element(xpath().ImageView(attr="content-desc='服务按钮'").draw):
            self.log.info('点击消息按钮')
            self.app.find_element(xpath().ImageView(attr="content-desc='消息'").draw).click()
        self.log.info('发送文本信息：{0}'.format(keyword))
        self.app.find_element(xpath().EditText(attr="resource-id='com.tencent.mm:id/a5e'").draw).send_keys(keyword)
        # self.app.find_element(xpath().Attribute("class='android.widget.EditText'").draw).send_keys(keyword)
        self.log.info('点击发送按钮')
        self.app.find_element(xpath().Button(attr="text='发送'").draw).click()

    def find_service(self,menu):
        '''
        点击菜单栏的按钮
        :info: find_service(['客服','小兰'])
        :param menus: list类型，根据list中按钮名称的顺序点击公众号下方的按钮
        :return: None
        '''
        if not self.app.find_element(xpath().ImageView(attr="content-desc='消息'").draw):
            self.log.info('点击服务按钮')
            self.app.find_element(xpath().ImageView(attr="content-desc='服务按钮'").draw).click()
        for key in menu:
            self.log.info('点击{0}按钮'.format(key))
            self.app.find_element(xpath().Attribute("text='{0}'".format(key)).draw).click()
            time.sleep(1)

    def get_last_agent_msg(self):
        '''
        获取最后一条坐席发送的信息
        :return: 文本信息
        '''
        time.sleep(5)
        last_msg = self.app.find_elements(self.__test_public_view_list__)[-1]
        if self.app.find_element(self.__test_public_agent_icon__,obj=last_msg):
            if self.app.find_element(self.__text_msg__,obj=last_msg).get_attribute('text'):
                self.log.info('获取{0}最后的消息类型为文本信息'.format(self.code))
                return self.app.find_element(self.__text_msg__,obj=last_msg).get_attribute('text')
            elif self.app.find_element(self.__image_msg__,obj=last_msg):
                self.log.info('获取{0}最后的消息类型为图片'.format(self.code))
                return 'picture'
            else:
                self.log.info('获取{0}最后的消息类型为未知'.format(self.code))
                return 'other type'
        else:
            self.log.info('获取{0}最后的消息类型为模板消息'.format(self.code))
            return 'template'


    def get_last_ucp_image(self):
        '''
        获取最后一条坐席发送的图片，主要是用作二维码识别时用的
        :return: element_object
        '''
        time.sleep(5)
        last_msg = self.app.find_elements(self.__ucp_view_list__)[-1]
        if self.app.find_element(self.__ucp_agent_icon__,obj=last_msg):
            self.log.info('获取统一通讯平台服务号最后一条二维码信息')
            return self.app.find_element(self.__image_msg__,obj=last_msg)
        raise self.log.error('获取统一通讯平台服务号最后一条二维码信息失败')

    @property
    def __ucp_view_list__(self):
        return self.__chat_list_view__(self.main_entry)

    @property
    def __ucp_agent_icon__(self):
        return self.__agent_icon__(self.main_entry)

    @property
    def __test_public_view_list__(self):
        return self.__chat_list_view__(self.public_name)

    @property
    def __test_public_agent_icon__(self):
        return self.__agent_icon__(self.public_name)

    @property
    def __image_msg__(self):
        return xpath().LinearLayout().LinearLayout().FrameLayout().ImageView().draw

    @property
    def __text_msg__(self):
        return xpath().LinearLayout().LinearLayout().TextView().draw

    def __agent_icon__(self,public_name):
        '''
        公众号坐席头像XPATH，需要在 __chat_list_view__ 后使用
        :return: XPATH
        '''
        attr = "content-desc='{0}头像'".format(public_name)
        self.log.info('获取【{0}】发送的消息 '.format(self.code))
        x= xpath().LinearLayout().\
                      RelativeLayout().\
                      Attribute(attr=attr).draw
        return x
    def __chat_list_view__(self,public_name):
        '''
        公众号聊天对话窗口XPATH
        :return: XPATH
        '''
        attr = 'content-desc="当前所在页面,与{0}的聊天"'.format(public_name)
        self.log.info('获取【{0}】聊天信息列表'.format(self.code))
        x= xpath().FrameLayout(attr=attr) \
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
        return x
