# -*- coding: utf-8 -*-
# 生成数值序列1-9，赋给i变量
for i in range(1,10):
    # 生成数值序列1到i+1（每次循环+1），赋给j变量
    for j in range(1,i+1):
        print '%d*%d=%d' %(j,i,j*i),
    print