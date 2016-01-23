# -*- coding: utf-8 -*-
# 习题 20: 函数和文件 

# 导入argv模组
from sys import argv

# argv解包，传递两个参数
script, input_file = argv

# 定义函数print_all，参数f
def print_all(f):
	# 读取文件内容并打印
	print f.read()

# 定义函数rewind，参数f
def rewind(f):
	# seek(0)，将文件定位到起始位置
	f.seek(0)

# 定义函数prnt_a_line，两个参数
def print_a_line(line_count, f):
	# readline()，读取文件中的一行
	print line_count, f.readline()
	
# 打开input_file文件
current_file = open(input_file)

# 打印字符串并换行
print "First let's print the whole file:\n"	

# 调用变量：读取文件内容并打印
print_all(current_file)

# 打印字符串
print "Now let's rewind, kind of like a tape."

# 调用rewind函数
# rewind(current_file)	

# 打印字符串
print "Let's print thrss lines:"

# 定义变量
current_line = 1
# 调用print_a_line函数，打印第一行
print_a_line(current_line, current_file)

# 定义变量
current_line = current_line + 1
# 调用print_a_line函数，打印第二行
print_a_line(current_line, current_file)

# 定义变量
current_line = current_line + 1
# 打印第三行
print_a_line(current_line, current_file)

# readline() 是怎么知道每一行在哪里的？ readline() 里边的代码会扫描文件的每一个字节，直到找到一个 \n 为止，
#然后它停止读取文件，并且返回此前的文件内容。文件f会记录每次调用 readline() 后的读取位置，这样它
#就可以在下次被调用时读取接下来的一行了。 