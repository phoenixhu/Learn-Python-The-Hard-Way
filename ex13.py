# -*- coding: utf-8 -*-
# 习题 13: 参数、解包、变量

# 导入argv模块
from sys import argv

# 把argv解包，将所有的参数一词赋予左边的变量名
script, first, second, third = argv

# 打印变量
print "The script is called:", script
print "Your frist variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third