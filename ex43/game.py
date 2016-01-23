# -*- coding: utf-8 -*-
from sys import exit
from random import randint

class game():
    list1 = [randint(1, 5), randint(4, 8), randint(12, 20)]
    list2 = [list1[0] * '*', list1[1] * '*', list1[2] * '*']
    number1 = 0
    number2 = 3
    def fangfa(self):
        game.number1 += 1
        print "你进入了一个门，门里有很多宝藏，但是门需要密码才能解开\n%s" % game.list2
        while True:
            self.a = int(raw_input("你看到了三道密码锁，猜猜第一道锁密码\n%s\n请输入：" % game.list2[0]))
          
            print game.list2[0]
            if self.a == game.list1[0]:
                game.list2[0] = self.a 
                print "你猜对了！\n%s" % game.list2
                break
            else:
                if game.number2 <= 3 and game.number2 != 1:
                    game.number2 -= 1
                    print "你猜错了,还有%d次机会" % game.number2
                else:
                    print "游戏结束，你失败了！"
                    exit(1)
        while True:
            self.a = int(raw_input("你已经解开了第一道锁，猜猜第二道锁密码\n%s\n请输入：" % game.list2[1]))
            
            print game.list2[1]
            if self.a == game.list1[1]:
                game.list2[1] = self.a 
                print "你猜对了！\n%s" % game.list2
                break
            else:
                if game.number2 <= 3 and game.number2 != 1:
                    game.number2 -= 1
                    print "你猜错了,还有%d次机会" % game.number2
                else:
                    print "游戏结束，你失败了！"
                    exit(1)      
 
        while True:
            self.a = int(raw_input("还有最后一道锁，宝藏将展现在你面前，猜猜第三道锁密码\n%s\n请输入：" % game.list2[2]))
                              
            print game.list2[2]
            if self.a == game.list1[2]:
                game.list2[2] = self.a 
                print "你猜对了,你得到了宝藏！\n%s" % game.list2
                exit(0)
            else:
                if game.number2 <= 3 and game.number2 != 1:
                    game.number2 -= 1
                    print "你猜错了,还有%d次机会" % game.number2
                else:
                    print "游戏结束，你失败了！"
                exit(1)                       