# -*- coding: utf-8 -*-
# 习题 11: 提问 

# 打印：你多大了？
print "How old are you?"

# 用户输入函数
age = raw_input()

# 打印：你多高？
print "How tall are you?"

# 用户输入函数
height = raw_input()

# 打印：你有多重？ 用户输入函数
print "How much do you weigh?",
weight = raw_input()

# 格式化字符串，打印用户的年龄、身高、体重
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)