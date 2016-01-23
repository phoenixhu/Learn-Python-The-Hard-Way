# -*- coding: utf-8 -*-
# 习题 4: 变量(variable)和命名 

# 数字变量赋值
cars = 100
space_in_a_car = 4.0 # 小数点会计算出浮点型，不加小数点会计算出整形
drivers = 30
passengers = 90

# 变量计算
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# 输出结果
print "There are", cars, "cars available." # cars=100
print "There are only", drivers, "drivers available." # drivers=30
print "There will be", cars_not_driven, "empty cars today." # cars_not_driven=70
print "We can transport", carpool_capacity, "people today." # carpool_capacity=120
print "We hava", passengers,  "to carpool today." # passengers=90
print "We need to put about", average_passengers_per_car, "in each car." # average_passengers_per_car=3
