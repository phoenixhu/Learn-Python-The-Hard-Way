# -*- coding: utf-8 -*-
# 习题 6: 字符串(string)和文本

# 将10格式化为整型并将这段字符串赋值给x
x = "There are %d types of people." % 10
# 定义变量
binary = "binary"
do_not = "don't"
# 将binary, do_not格式化为字符串并将这段字符串赋值给y
y = "Those who konw %s and those who %s." % (binary, do_not)

# 打印结果
print x
print y

# 把x的变量值格式化为对象并打印，结果：I said: "There are 10 types of people."
print "I said: %r." % x
# 把y的变量值格式化为字符串并打印，结果：I also said: 'Those who konw binary and those who do_not'.
print "I also said: '%s'." % y

# 定义变量为Flase
hilarious = False
# 定义变量
joke_evaluation = "Isn't that joke so funny?! %r" 
# 打印joke_evaluation变量值然后格式化字符串，结果：Isn't that joke so funny?! False
print joke_evaluation % hilarious

# 定义变量
w = "This is the left side of..."
e = "a string with a right side"
# 变量拼接
print w + e