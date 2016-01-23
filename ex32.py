# -*- coding: utf-8 -*-

# 定义三个列表
the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
changs = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# 循环the_count列表，把值赋给number变量
# this first kind of for-loop goes through a list
for number in the_count:
    # 打印number值
    print "This is count %d" % number

# 循环fruits列表，把值赋给fruit变量    
# same as above
for fruit in fruits:
    # 打印fruit值
    print "A fruit of type: %s" % fruit

# 循环change列表，把值赋给i变量     
# also we can go through mixed lists too
# notice we have to use %r since we don't konw what's in it
for i in changs:
    # 打印i值
    print "I got %r" % i
    
# 定义一个空列表
# we can also build lists, first start with an empty one
elements = []

# ranfe()函数生成一个数值序列，起始位置为0，结束位置为5，并把值赋给变量i开始循环
# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    # 打印i值
    print "Adding %d to the list." % i
    # 使用append()函数，将数值序列添加到空列表中
    # append is a function that lists understand
    elements.append(i)

# 循环elements列表，把值赋给i变量  
# now we can print them out too
for i in elements:
    # 打印i值
    print "Element was: %d" % i