# -*- coding: utf-8 -*-

# 定义一段字符串
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# 打印字符串
print "Wait there's not 10 thing in that list, let's fix that."

# split()方法是对字符串进行切片，参数是分隔符和分隔次数，最终切片的返回值是个列表
# ten_tings变量引用split()方法进行切片，分隔符是空格，然后把切片出的列表赋给stuff变量
stuff = ten_things.split(' ')

# 定义一个列表
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn",
"Banana", "Girl", "Boy"]

# len()函数计算元素个数
# 如果stuff的元素个数不等于10，此表达式成立True，开始循环语句块内容，一旦循环到等于10，此表达式不成立Flase，结束循环
while len(stuff) != 10:
    # pop()方法移除列表中的元素，参数是列表的位置编号，不加参数默认从列表中的最后位置移除，最终会返回已删除的元素
    # more_stuff引用pop()方法，开始从最后位置移除元素，然后把返回的移除元素赋给next_one变量_
    next_one = more_stuff.pop()
    
    # 打印移除后元素
    print "Adding: ", next_one
    
    # stuff引用append方法，将移除后的元素再添加到stuff列表的最后位置
    stuff.append(next_one)
    
    # 统计stuff列表的个数
    print "There's %d items now." % len(stuff)
    
# 以上共成功循环了四次，第五次循环发现stuff列表的个数等于10，为False，循环结束

# 打印stuff列表    
print "There we go: ", stuff

# 打印字符串
print "Let's do some things with stuff."

# 打印第2个元素
print stuff[1]

# 打印最后一个元素
print stuff[-1]

# 移除最后一个元素并将元素打印
print stuff.pop()
print stuff
# join()方法是通过指定的字符元素将列表或元组中的元素连接，最后返回连接后的字符串，参数是要连接的对象
# 空格引用join方法，将参数stuff列表用空格连接，最后打印连接后的字符串
print ' '.join(stuff)

# #号引用join方法，将参数stuff列表第4-5位置的元素用#号连接，最后打印连接后的字符串
print '#'.join(stuff[3:5])
    