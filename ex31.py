# -*- coding: utf-8 -×-

# 打印字符串
print "You enter a dark room with two doors. doyou go thrugh #1 or door #2?"

# 提示用户输入字符串
door = raw_input("> ")

# 判断1：如果用户输入的为“1”，开始执行缩进区域代码
if door == "1":
    # 打印字符串
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1. Take the cake."
    print "2. scream at the bear."
    
    # 继续提示用户输入字符串
    bear = raw_input("> ")
    
    # 判断1：如果用户输入的为“1”，开始执行缩进区域代码
    if bear == "1":
        print "The bear eats your face off. Good job!"
    # 判断2：如果用户输入的为“2”，开始执行缩进区域代码
    elif bear == "2":
        print "The bear catsyour legs off. Good job!" 
    # 以上判断都不是，开始执行缩进区域代码    
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

# 判断2：如果用户输入的为“2”，开始执行缩进区域代码
elif door == "2":
    # 打印字符串
    print "You stare into the endless abyss at Cthulu's retina." 
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."
    
    # 继续提示用户输入字符串
    insanity = raw_input("> ")
    
    # 判断：或运算，如果输入的是“1”或者是“2”，开始执行缩进区域代码
    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. Good job!"
    # 以上判断都不是，开始执行缩进区域代码  
    else:
        print "The insanity rots your eyes into a pool of  muck. Good job!"

# 以上判断都不是，开始执行缩进区域代码
else:
    print "You stumble around and fall on a knife and die. Good job!"       
                    