# -*- coding: utf-8 -*-
class TheThing(object):
    
    def __init__(self):
        self.number = 0
        
    def some_function(self):
        print "I got called."
        
    def add_me_up(self, more):
        self.number += more
        return self.number
    
# two different things
# 产生实例化对象
a = TheThing()
b = TheThing()

# 访问some_function实例方法
# 打印I got called.
a.some_function()
b.some_function()

# 访问add_me_up实例方法
# 打印结果：20
print a.add_me_up(20)
# 打印结果：20 
print b.add_me_up(30)

# 打印number变量的值
print a.number
print b.number

class TheMultiplier(object):
    
    def __init__(self, base):
        self.base = base
        
    def do_it(self, m):
        return m * self.base

# 产生实例化对象，参数引用a.number，即20   
x = TheMultiplier(a.number)
# 访问do_it实例方法，参数为b.number，即30
# 结果是600
print x.do_it(b.number)    