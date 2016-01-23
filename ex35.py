# -*- coding: utf-8 -*-

# 导入退出模组
from sys import exit

# 定义gold_room()函数
def gold_room():
    # 这个房间充满了黄金。你拿多少钱?
    print "This room is full of gold. How much do you take?"
    
    # 用户输入，赋给next
    next = raw_input("> ")
    # 如果用户输入的包含“0”或者是“1”：
    # in是一个布尔操作符，他测试左边的操作数是否包含于列表（适用于列表判断）
    if "0" in next or "1" in next:
        # 将用户输入的值转换为整型数字并赋给how_much变量
        how_much = int(next)
    # 否则：
    else:
        # 调用dead函数
        # 男人，你应该键入一个数字
        dead("Man, learn to type a number.")
    # 继续判断，如果用户输入的值小于50：    
    if how_much < 50:
        # 好,你不贪心,你赢了!
        print "Nice, you're not greedy, you win!"
        # 正常退出游戏
        exit(0)
    # 否则：    
    else:
        # 调用dead函数
        # 你是个贪婪的混蛋
        dead("You greedy bastard!")
 
# 定义bear_room()函数    
def bear_room():
    # 这是一只熊
    print "There is a bear here."
    # 这只熊有一堆的蜂蜜
    print "The bear has a bunch of honey."
    # 肥熊在另一个门口挡住了你的去路
    print "The fat bear is in front of another door."
    # 你打算如何移动熊？
    print "How are you going to move the bear?"
    # 定义bear_moved变量值为False
    bear_moved = False
    
    # 创建一个无限循环
    while True:
        # 用户输入，赋给next变量
        next = raw_input("> ")
        
        # 如果用户输入的是“take honey”
        if next == "take honey":
            # 调用dead函数
            # 熊看到你了，打了你的脸
            dead("The bear looks at you then slaps your face off.")
        # 如果用户输入的是"taunt bear" 
        # 执行后进行循环
        # 在输入taunt bear循环后，bear_moved变量值已经变为了True，如果再次输入"taunt bear" ，此判断不会成立，继续下一个判断
        elif next == "taunt bear" and not bear_moved:
            # 熊已经从门口走开，你现在可以通过这道门
            print "The bear has moved from the door. You can go through it now."
            # bear_moved变量值改为为True
            bear_moved = True
        # 如果用户输入的是"taunt bear"    
        # 在输入taunt bear循环后，bear_moved变量值已经变为了True，此判断成立
        elif next == "taunt bear" and bear_moved:
            # 调用dead函数
            # 熊变得生气,咬你的腿。
            dead("The bear gets pissed off and chews your leg off.")
        # 如果用户输入的是"open door"  
        # 第一次循环直接输入open door，因bear_moved变量值为False，此判断布尔值不成立，继续下一个判断
        # 在输入taunt bear循环后，bear_moved变量值已经变为了True，此判断成立
        elif next == "open door" and bear_moved:
            # 调用gold_room函数
            gold_room()
        # 如果以上判断都不是：
        else:
            # 我不知道这是什么意思
            print "I got no idea what that means."
            
# 定义cthulhu_room()函数            
def cthulhu_room():
    # 在这里，你看到的巨大恶魔邪神
    print "Here you see the great evil Cthulhu."
    # 他一直在盯着你，你快要疯了
    print "He, it, whatever stares at you and you go insane."
    # 你选择逃离还是被它吃头？
    print "Do you flee for your life or eat your head?"
    
    # 用户输入，赋给next变量
    next = raw_input("> ")
    # 如果用户输入的包含“fell”
    if "flee" in next:
        # 调用start()函数
        start()
    # 如果用户输入的包含“head”    
    elif "head" in next:
        # 调用dead()函数
        # 这是美味的
        dead("Well that was tasty!")
    # 以上判断都不是：
    else:
        # 调用cthulhu_room()函数
        cthulhu_room()

# 定义dead()函数，一个参数 
def dead(why):
    # 打印参数和一个字符串“干的好！”
    print why, "Good job!"
    # 正常退出游戏
    exit(0)

# 定义start()函数    
def start():
    # 你是在一个黑暗的房间
    print "You are in a dark room."
    # 你的左边和右边都有一扇门
    print "There is a door to your right and left."
    # 你要走哪一个？
    print "Which one do you take?"
    
    # 用户输入，赋给next变量
    next = raw_input("> ")
    
    # 如果用户输入的是“left”
    if next == "left":
        # 调用bear_room()函数
        bear_room()
    # 如果用户输入的是“right”
    elif next == "right":
        # 调用cthulhu_room()函数
        cthulhu_room()
    # 如果以上判断都不是：
    else:
        # 调用dead()函数
        # 您绊倒在房间里，直到饿死。
        dead("You stumble around the room until you starve.")

# 调用start()函数开始游戏                                   
start()                            