# -*- coding: utf-8 -*-
# 习题 12: 提示别人

# raw_input函数，提示用户输入字符串
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)
	