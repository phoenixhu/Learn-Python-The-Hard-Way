# -*- coding: utf-8 -*-
# 读取filename文件

from sys import argv
script, filename = argv
txt = open(filename)
print txt.read()
txt.close()