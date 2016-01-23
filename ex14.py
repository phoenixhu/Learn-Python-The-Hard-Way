# -*- coding: utf-8 -*-
#习题 14: 提示和传递

# 导入argv模组
from sys import argv

# argv解包，定义参数变量，script为脚本名称，user_name为第一参数，man为第二参数
script, user_name, man = argv
# 定义变量
prompt = '>'
# 打印参数
print "Hi %s, I'm the %s script, You are a %s person!" % (user_name, script, man)
# 打印字符串
print "I'd like to ask you a few questions."

# 打印参数值
print "Do you like me %s?" % user_name
# 引入prompt的值">",提示用户输入字符串
likes = raw_input(prompt)

# 打印参数
print "Where do you live %s?" % user_name
# 引入prompt的值">",提示用户输入字符串
lives = raw_input(prompt)

# 打印字符串
print "What kind of computer do you have?" 

# 引入prompt的值">",提示用户输入字符串
computer = raw_input(prompt)

# 格式化字符串，显示likes, lives, computer, age这四个变量用户输入的内容
print """
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)