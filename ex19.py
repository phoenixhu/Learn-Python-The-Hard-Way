# -*- coding: utf-8 -*-
# 习题 19: 函数和变量

# 定义一个函数，需要两个参数
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"

# 打印字符串	
print "We can just give the function numbers directly:"
# 调用函数
cheese_and_crackers(20, 30)


# 打印字符串
print "OR, we can use variables from our script:"
# 定义变量
amount_of_cheese = 10
amount_of_crackers = 50

# 调用函数，参数引入定义变量的值
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# 打印字符串
print "We can even do math inside too:"
# 调用函数，参数使用整型相加
cheese_and_crackers(10 + 20, 5 + 6)

# 打印字符串
print "And we can combine the two, variables and math:"
# 调用函数，参数引入定义变量的值并加整型数字
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)