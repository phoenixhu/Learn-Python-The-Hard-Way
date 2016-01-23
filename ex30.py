# -*- coding: utf-8 -*-

# 定义初始变量
people = 30
cars = 40
buses = 15

# 判断1：如果cars > people，执行print语句(True)
if cars > people:
    print "We should take the cars."
# 判断2：如果cars < people，执行print语句    
elif cars < people:
    print "We should not take the cars."
# 如果都不成立，执行print语句    
else:
    print "We can't decide."
    
# 判断1：如果buses > cars，执行print语句
if buses > cars:
    print "That's too many buses."
# 判断2：如果buses < cars，执行print语句(True)    
elif buses < cars:
    print "Maybe we could take the buses."
# 如果都不成立，执行print语句
else:
    print "We still can't decide."

# 判断：如果布尔值成立，执行print语句(True)
if people > buses and not (buses > people or cars < buses):
    print "Alright, let's just take the buses."
# 如果都不成立，执行print语句
else:
    print "Fine, let's stay home then." 
           