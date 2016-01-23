# -*- coding: utf-8 -*-

# 字符串打印
print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"
# 字符串打印结束

# 定义一个变量值，5
five = 10 - 2 + 3 - 6
# 打印变量值
print "This should be five: %s" % five

# 定义函数
def secret_formula(started):
	jelly_beans = started * 500
	jars = jelly_beans / 1000
	crates = jars / 100
	return jelly_beans, jars, crates
	
# 定义一个变量值
start_point = 10000
# 调用secret_foumula函数，参数引用start_point变量，将计算返回值分别赋给三个变量，beans=5000000 jars=5000 crates=50
beans, jars, crates = secret_formula(start_point)

# 打印变量的值
print "With a starting point of: %d" % start_point
# 打印三个变量的计算结果
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

# 重新定义变量值，10000 / 10
start_point = start_point / 10

# 打印字符串
print "We can also do that this way:"
# 调用函数并计算结果，参数引用start_point变量，将计算返回值分别格式化，500000，500，5 
print "We'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)