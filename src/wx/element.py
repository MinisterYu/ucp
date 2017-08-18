#coding:utf-8

class root():

    def __init__(self,e='/'):
        self.e = e

    def Attribute(self,attr,index=0):
        e = ''
        if not index:
            e += '/*[@{0}]'.format(attr)
        else:
            e += '/*[@{0}][{1}]'.format(attr,index)
        self.e += e
        return root(self.e)

    def FrameLayout(self,index=0,attr=''):
        e = '/android.widget.FrameLayout'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return root(self.e)

    def LinearLayout(self,index=0,attr=''):
        e = '/android.widget.LinearLayout'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return root(self.e)

    def ListView(self,index=0,attr=''):
        e = '/android.widget.ListView'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return root(self.e)

    def RelativeLayout(self,index=0,attr=''):
        e = '/android.widget.RelativeLayout'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return root(self.e)

    def ViewGroup(self,index=0,attr=''):
        e = '/android.view.ViewGroup'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return root(self.e)

    def TextView(self,index=0,attr=''):
        e = '/android.widget.TextView'
        if attr :
            e += '[@{0}]'.format(attr)
        if index:
            e += '[{0}]'.format(index)
        self.e += e
        return root(self.e)

    @property
    def draw(self):
        return self.e


if __name__ == '__main__':
    print root().FrameLayout(attr='content-desc="当前所在页面,与统一通讯平台服务号的聊天"')\
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
            .ListView()\
            .RelativeLayout(1).LinearLayout().LinearLayout().LinearLayout().TextView().draw
