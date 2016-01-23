# -*- coding: utf-8 -*-
# create a mapping of state to abbreviation
# 创建字典,冒号前是“键”，冒号后是“值”
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
# 创建字典 
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
# 增加字典
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
# 将-打印10遍
print '-' * 10
# 打印 New York
print "NY State has: ", cities['NY']
# 打印 Portland
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
# 打印 MI
print "Michigan's abbreviation is: ", states['Michigan']
# 打印 FL
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '-' * 10
# 从内往外开始计算，states['Michigan']是MI，cities['MI']是Detroit
print "Michigan has: ", cities[states['Michigan']]
# 打印 Jacksonville
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
# 返回为列表，列表中包含元组，字典包含在元组中，然后对每个元组中的键,值遍历
for state, abbrev in states.items():
    # 打印每个元组中的两个值
    print "%s is abbrebiate %s" % (state, abbrev)


# print every city in state
print '-' * 10
# 返回为列表，列表中包含元组，字典包含在元组中，然后对每个元组中的键,值遍历
for abbrev, city in cities.items():
    # 打印每个元组中的两个值
    print "%s has the city %s" % (abbrev, city)
    
# now do both at the same time
print '-' * 10
# 返回为列表，列表中包含元组，字典包含在元组中，然后对每个元组中的键,值遍历
for state, abbrev in states.items():
    # 打印元组中的两个值及cities[abbrev]对应的值
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
# 查询states字典中的‘Texas’如果不存在，返回默认值None
state = states.get('Texas', None)
# 如果没有查到，执行语句块代码
if not state:
    print "Sorry, no Texas."
    
# get a city with a default value
# 查询citis中的‘TX’,如果查询不到，显示返回为Does Not Exist
city = cities.get('TX', 'Does Not Exist')
# 打印查询结果
print "The city for the state 'TX' is: %s" % city            
    
    