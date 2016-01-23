# -*- coding: utf-8 -*-
# 习题 10: 那是什么？ 

# \t转义为制表符，相当于一个tab键空格
tabby_cat = "\ti'm tabbed in."
# \n转移换行
persian_cat = "I'm split\non a line."
# \\转移转义为一个\符号
backslash_cat = "I'm \\ a \\ cat."

# 多行换行输出，\t转义空格
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

# 打印变量
print tabby_cat
print persian_cat
print backslash_cat
print fat_cat