# -*- coding: utf-8 -*-

# 将转义序列和格式化字符串组合到一起，创建一种更复杂的格式
name = "huping\nhuan"
age = "\n\t%s\n\t%s"
print "%s" % name
print age % ("13", "15")

# 记得 %r 格式化字符串吗？使用 %r 搭配单引号和双引号转义字符打印一些字符串出来。将 %r 和 %s 比较一下。
name = "huping\"22\"'1993'"
# 返回值为'huping"22"\'1993\''
print "%r" % name 
print "%s" % name