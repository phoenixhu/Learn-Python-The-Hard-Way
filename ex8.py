# -*- coding: utf-8 -*-
# 习题 8: 打印，打印

# 定义变量为格式化字符%r
formatter = "%r %r %r %r"
# 打印1 2 3 4
print formatter % (1, 2, 3, 4)
# 打印‘one’ ‘two’ ‘three’ ‘four’
print formatter % ("one", "two", "three", "four")
# 打印True False False True
print formatter % (True, False, False, True)
# 打印 '%r%r%r%r' '%r%r%r%r' '%r%r%r%r' '%r%r%r%r'
print formatter % (formatter, formatter, formatter, formatter)
# 打印以下字符串
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight"
)	