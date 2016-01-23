# -*- coding: utf-8 -*-
import time
class times(object):
    intime = time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()))
    def __init__(self):	
        print "当前系统时间是：%s"  % times.intime