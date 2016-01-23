# -*- coding: utf-8 -*-
# 习题 5: 更多的变量和打印

# 定义变量
my_name = 'Zed A. Shaw' #姓名
my_age = 35 # not a lie 年龄
my_height = 74 * 2.54 # inches 身高英寸转换为厘米
my_weight = 180 * 0.454 # lbs 体重磅转换为千克
my_eyes = 'Blue' # 眼睛
my_teeth = 'White' # 牙齿
my_hair = 'Brown' # 头发

# 将my_name格式化为字符串（%s）
print "Let's talk about %s." % my_name
# 将my_height格式化为整数（%d）
print "He's %d inches tall." % (my_height)
# 将my_weight格式化为整数（%d）
print "He's %d pounds heavy." % (my_weight)
# 打印字符串
print "Actually that's not too heavy."
# 将my_eyes, my_hair格式化为字符串（%s），多个变量应括()起来
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
# 将my_teeth的变量值都打印出来，包含''符号（%r）
print "His teeth are usually %r depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
# 打印字符串If I add 35, 74, and 180 I get 289.
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

