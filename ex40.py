# -*- coding: utf-8 -*-

# 定义一个字段字段
cities = {'CA': 'San Francisco', 'MI': 'Detroit',
                    'FL': 'Jacksonville'}
                    
# 循环打印了cities['CA']值的每一个字符
for i in cities['CA']:
    print i

# items()方法返回可遍历的元组数据
for x, y in cities.items():
    # 打印字典中每个键和值
    print "%s:%s" % (x, y)    

# 字典中再增加两个元素                    
cities['NY'] = 'New York' 
cities['OR'] = 'Portland'

# 定义函数，此函数判断用户给的值能不能在字典中找到，themp参数是字典对象，state是用户输入对象，即要查找的字典键
def find_city(themap, state):
    
    # 如果themp字典中包含state值
    if state in themap:
        # 将该字典键的值返回
        return themap[state]
    
    # 如果不包含
    else:
        
        # 返回字符串，没有找到
        return "Not found."

# 将函数加入到字典中    
cities['_find'] = find_city

# 进入一个无限循环
while True:
    
    # 打印字符串，提示用户输入要查找的键
    print "State? (ENTER to quit)",
    
    # 得到用户输入，并将键赋给state变量
    state = raw_input("> ")
    
    # 如果用户按的是回车，表示这是一个“”空字符串，为False，not state表达式成立，退出循环
    if not state: break

    # 调用字典中的find_city()函数，查询字典中用户给的键
    city_found = cities['_find'](cities, state)
    
    # 将结果输出
    print city_found