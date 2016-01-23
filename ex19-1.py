# -*- coding: utf-8 -*-

def test_one(filename_one, filename_two):
	from os.path import exists
	print "Copying from %s to %s" % (filename_one, filename_two)
	print "Cancel Ctrl + c, determined Enter"
	raw_input("?")
	in_file = open(filename_one)
	
	to_file = in_file.read()
	
	print "The input file is %d bytes long" % len(to_file)
	print "Does the output file exist? %r" % exists(filename_two)
	out_file = open(filename_two, 'w') # 没有定义变量导致错误
	out_file.write(to_file) # 没有定义变量导致错误
	print "Copy complete!"
	out_file.close()
	in_file.close()
test_one("test.txt", "test2.txt") # 因没有加上双引号导致程序运行错误