#coding:utf-8
import time

class Logger():

    def __init__(self,level='debug'):
        self.level = level
        self.check = {'debug':0,'info':1,'warn':2,'error':3}

    @property
    def now(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    def debug(self,debug):
        check = self.check[self.level]
        if check < 1:
            print '{1}[DEBUG]:{0}'.format(debug,self.now)

    def info(self,info):
        check = self.check[self.level]
        if check < 2:
            print '{1}[INFO]:{0}'.format(info,self.now)

    def warn(self,warn):
        check = self.check[self.level]
        if check < 3:
            print '{1}[WARN]:{0}'.format(warn,self.now)

    def error(self,error):
        print '{1}[ERROR]:{0}'.format(error,self.now)
