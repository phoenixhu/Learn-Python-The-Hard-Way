# -*- coding: utf-8 -*-
from game import *
dict = {}
class info():
    
    def __init__(self):
        self.username = raw_input("请输入姓名：")
        global dict
        dict['name'] = self.username
        self.userage = raw_input("请输入您的年龄:")
        dict['age'] = self.userage
        if int(dict['age']) < 18:
            print "您未满18岁！"
        elif int(dict['age']) >= 18:
            self.two = game()  
            self.two.fangfa()                