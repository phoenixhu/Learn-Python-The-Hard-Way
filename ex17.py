# -*- coding: utf-8 -*-
# 习题 17: 更多文件操作

# 导入argv模组，让用户执行脚本的时候给出参数
from sys import argv
# 导入exists模组，检查文件是否存在
from os.path import exists

# argv解包，定义参数变量
script, from_file, to_file = argv

# 打印用户的参数
print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
# 打开from_file文件
in_file = open(from_file)
# 读取from_file文件内容
indata = in_file.read()

# 查看from_file文件长度
print "The input file is %d bytes long" % len(indata)

# 检查to_file是否存在，存在返回 True，否则返回 False
print "Does the output file exist? %r" % exists(to_file)
# 提示用户回车继续，CTRL-C中止
print "Ready, hit RETURN to continue, CTRL-C to abort."
# 用户输入
raw_input()

# 可写入模式打开to_file文件
out_file = open(to_file, "w")
# 将from_file文件内容写入到out_file文件中
out_file.write(indata)

# 提示完成
print "Alright, all done."

# 把两个文件关闭
out_file.close()
in_file.close()