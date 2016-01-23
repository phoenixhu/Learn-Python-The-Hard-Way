# -*- coding: utf-8 -*-
# 习题 18: 命名、变量、代码、函数

# this one is like your scripts with argv

# 定义函数print_two
def print_two(*args):
    # 将函数解包，args有两个参数
	arg1, arg2 = args
	# 打印参数
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# ok, that *args is actually polintless, we can just do this
# 定义函数print_two_again,有两个参数
def print_two_again(arg1, arg2):
    # 打印参数
	print "arg1: %r, arg2: %r" % (arg1, arg2)
	
# this just takes one argument
# 定义函数print_one，有一个参数
def print_one(arg1):
    # 打印参数
	print "arg1: %r" % arg1

# this one takes no arguments
# 定义函数print_none，没有参数
def print_none():
    # 打印这段字符串
	print "I got nothin'."

# 以下部分为调用定义的函数，实现函数里的功能
print_two("Zed","Shaw")
print_two_again("Zed","Shaw")
print_one("First!")
print_none()	