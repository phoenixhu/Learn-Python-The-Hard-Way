# -*- coding: utf-8 -*-

# 定义两个初始变量
i = 0
numbers = []

# 开始while循环，直到i < 6为false时停止循环
while i < 6:#
    # 打印循环的i值
    print "At the top i is %d" % i
    # 每次循环的i值添加到numbers列表中
    numbers.append(i)
    
    # 每次循环i变量的值+1
    i = i + 1
    # 打印numbers列表
    print "Numbers now: ", numbers
    # 打印+1后i变量值
    print "At the bottom i is %d" % i

# 打印字符串    
print "The numbers: "

# 循环打印numbers列表的值
for num in numbers:
    print num    
    