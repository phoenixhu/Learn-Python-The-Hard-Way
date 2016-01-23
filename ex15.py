# -*- coding: utf-8 -*-
# 习题 15: 读取文件

# 导入argv模组
from sys import argv

# argv解包
script, filename = argv

# 打开filename文件
txt = open(filename)

# 打印filename的文件名
print "Here's your file %r:" % filename

# read函数读取txt变量内容
print txt.read()

# 提示用户再次输入文件名
print "Type the filename again:"
file_again = raw_input("> ")

# 打开文件名
txt_again = open(file_again)

# read函数读取txt_again变量内容
print txt_again.read()