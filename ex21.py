# -*- coding: utf-8 -*-
# 习题 21: 函数可以返回东西

# 定义加法函数
def add(a, b):
	# 打印函数的功能
	print "ADDING %d + %d" % (a, b)
	# 回传计算结果（只是把结果返回，不会打印出来，把结果返回后定义给变量）
	return a + b

# 定义减法函数	
def subtract(a, b):
	# 打印函数的功能
	print "SUBTRACTING %d - %d" % (a, b)
	# 回传计算结果
	return a - b

# 定义乘法函数	
def multiply(a, b):
	# 打印函数的功能
	print "MULTIPLYING %d * %d" % (a, b)
	# 回传计算结果
	return a * b
# 定义除法函数	
def divide(a, b):
	# 打印函数的功能
	print "DIVIDING %d / %d" % (a, b)
	# 回传计算结果
	return a / b

# 打印函数的功能	
print "Let's do some math with just functions!"

# 调用四则函数并将回传（return）计算结果赋值给变量
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# 格式化字符串显示各计算结果
print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)


# A puzzle for the extra credit, type it in anyway.
# 打印字符串
print "Here is a puzzle."

# 由内外外开始计算，最后计算加法，把回传结果赋值给变量
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# 也可以用以下拆解方法计算
# test1 =  divide(iq, 2)
# test2 =  multiply(weight, test1)
# test3 =  subtract(height, test2)
# what = add(age,test3)

# 打印计算结果
print "That becomes: ", what, "Can you do it by hand?"