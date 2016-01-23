# -*- coding: utf-8 -*-
# 习题 16: 读写文件 

# 导入argv模组
from sys import argv

# 解析argv
script, filename = argv

# 提示用户会清除filename这个文件里的内容
print "We're going to erase %r." % filename
# 提示用户如果要取消按CTRL-C键
print "If you don't want that, hit CTRL-C (^C)."
# 提示用户如果继续按回车
print "If you do want that, hit RETURN."

# 用户输入
raw_input("?")

# 提示打开文件
print "Opening the file..."
# 打开filename文件并加上“w”参数，可写模式
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
# truncate清空文件内容
target.truncate()

print "Now I'm going to ask you for three lines."

# 提示用户输入三行字符串
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# 将用户输入的字符串拼接并换行
str = line1 + "\n" + line2 + "\n" + line3 + "\n"
# 写入用户输入的字符串到文件
target.write(str)


print "And finally, we close it."
# 关闭文件
target.close()