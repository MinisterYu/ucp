#coding:utf-8

class element():

    def __init__(self,e):
        self.e = e

    def Attribute(self,attr,index=0):
        e = ''
        if not index:
            e += '/*[@{0}]'.format(attr)
        else:
            e += '/*[@{0}][{1}]'.format(attr,index)
        self.e += e
        return element(self.e)

    def FrameLayout(self,attr='',index=0):
        e = '/android.widget.FrameLayout'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return element(self.e)

    def LinearLayout(self,attr='',index=0):
        e = '/android.widget.LinearLayout'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return element(self.e)

    def ListView(self,attr='',index=0):
        e = '/android.widget.ListView'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return element(self.e)

    def RelativeLayout(self,attr='',index=0):
        e = '/android.widget.RelativeLayout'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return element(self.e)

    @property
    def draw(self):
        return self.e


if __name__ == '__main__':
    print element('/').FrameLayout("content-desc='当前所在页面,与统一通讯平台服务号的聊天'").FrameLayout().LinearLayout().LinearLayout().ListView().draw