#coding:utf-8

class element():

    def __init__(self,e):
        self.e = e

    def Attribute(self,attr,index=0):
        if not index:
            self.e += '/*[@{0}]'.format(attr)
        else:
            self.e += '/*[@{0}][{1}]'.format(attr,index)
        return element(self.e)

    def FrameLayout(self,index=0):
        if not index:
            self.e += '/android.widget.FrameLayout'
        else:
            self.e += '/android.widget.FrameLayout[{0}]'.format(index)
        return element(self.e)

    def LinearLayout(self,index=0):
        if not index:
            self.e += '/android.widget.LinearLayout'
        else:
            self.e += '/android.widget.LinearLayout[{0}]'.format(index)
        return element(self.e)

    def ListView(self,index=0):
        if not index:
            self.e += '/android.widget.ListView'
        else:
            self.e += '/android.widget.ListView[{0}]'.format(index)
        return element(self.e)

    def RelativeLayout(self,index=0):
        if not index:
            self.e += '/android.widget.RelativeLayout'
        else:
            self.e += '/android.widget.RelativeLayout[{0}]'.format(index)
        return element(self.e)

    @property
    def draw(self):
        return self.e


if __name__ == '__main__':
    e = element('/')
    print e.Attribute("content-desc='当前所在页面,与统一通讯平台服务号的聊天'").draw