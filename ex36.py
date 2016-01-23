# -*- coding: utf-8 -*-
from sys import argv
from sys import exit

# 定义角色名参数
script, game_name = argv
renwu = []
difang = []
xue_rmb = [100, 500]
def game_huangye():
	global xue_rmb
	print "%s:欢迎来到%s，想要得到%s吗？需要支付给我300金币" % (renwu[4], difang[1], renwu[5])
	print """是否愿意支付，请输入数字选择：
	1.支付 
	2.不支付 
	"""
	zhifu = raw_input("请输入：")
	if zhifu == "1":
		xue_rmb[0] += 10
		xue_rmb[1] -= 300
		print "%s：你得到了一把%s，同时得到%s赠送的%d血值，你现在血值是：%d，金钱是：%d，你现在可以去找%s复仇了！" % (renwu[1], renwu[5], renwu[4], 10, xue_rmb[0], xue_rmb[1], renwu[0])
	else:
		print "%s：哼，这点钱都不愿意出，你回去吧！" % renwu[4]
		print "%s:你被%s送回到起点，游戏重新开始！" % (renwu[1], renwu[4])
		start_game(game_name_temp)
	boss_game()		
def game_true():
	global xue_rmb
	xue_rmb[0] += 20
	xue_rmb[1] += 50
def game_learn(game_name_temp):
	global renwu
	global difang
	renwu.append("荒野商人")
	renwu.append("AK47枪")
	difang.append("荒野城堡")
	
	print "%s：你就是传说中的%s吗？我想拜你为师，我被%s打了，我学复仇！" % (game_name_temp, renwu[3], renwu[0])
	print """%s：欢迎你，%s，来到%s，如果你想成为我的徒弟，必须能回答我的一些问题，
	一共有3道题，如果全部答对，便可收你为徒，并且会得到50血值和200金币作为奖励，
	如果答错其中一题，我不会收你为徒""" % (renwu[3], game_name_temp, difang[0])
	raw_input("准备好了吗？按任意键开始答题")
	
	print """%s：中国的第一部字典是：
	A.说文解字 
	B.辞海 
	C.康熙字典 
	D.新华字典
	""" % renwu[3]
	ti = raw_input("请属于答案字母：")
	if ti == "A":
		game_true()
		print "%s：恭喜你答对了，血值增加：%d，总共：%d，金钱增加：%d，总共：%d，继续下一题" % (renwu[3], 20, xue_rmb[0], 50, xue_rmb[1])
	else:
		dead("你答错了，我不能收你为徒弟！") 	
		
	print """%s：《赵氏孤儿》的故事记载最早见于：
	A.战国策 
	B.左传 
	C.史记 
	D.春秋
	""" % renwu[3]
	ti = raw_input("请属于答案字母：")
	if ti == "B":
		game_true()
		print "%s：恭喜你答对了，血值增加：%d，总共：%d，金钱增加：%d，总共：%d，继续下一题" % (renwu[3], 20, xue_rmb[0], 50, xue_rmb[1])
	else:
		dead("你答错了，我不能收你为徒弟！") 		

	print """%s：“弱冠”指的是男子多少岁:
	A.十五岁
	B.二十岁
	C.三十岁
	D.四十岁
	""" % renwu[3]
	ti = raw_input("请属于答案字母：")
	if ti == "B":
		game_true()
		print "%s：恭喜你答对了，血值增加：%d，总共：%d，金钱增加：%d，总共：%d，你可以作为我的徒弟了！" % (renwu[3], 20, xue_rmb[0], 50, xue_rmb[1])
	else:
		dead("你答错了，我不能收你为徒弟！") 			
	print "%s：你现在已经已经学会了我教你功夫，你可以下山了，下山往南走有个%s，去找一个叫%s的人，你他给你一把%s，你就可以找%s复仇了！"	 % (renwu[3], difang[1], renwu[4], renwu[5], renwu[0])		
	game_huangye()
def dead(str_temp):
	print str_temp, "你输了！"
	exit(0)
def boss_game():
	global xue_one
	if xue_rmb[0] < 100:
		dead("小兄弟，你还嫩！")
	elif xue_rmb[0] >= 100:
		print "你打败了%s" % renwu[0]
		exit(0)	
	else:
		dead("小兄弟，你还嫩！")	
def hospital_game():
	global renwu
	global difang
	renwu.append("医生")
	renwu.append("正义大师")
	difang.append("武林学院")
	print "%s：你的病情很严重，需要支付100金钱才能完成手术" % renwu[2]
	print """
	1. 治疗
	2. 不治疗
	"""
	xuanze_two = raw_input("确定要治疗吗？请选择：\n")
	if "1" in xuanze_two or "治疗" in xuanze_two:
		global xue_rmb
		xue_rmb[0] += 10
		xue_rmb[1] -= 100
		print "%s：你现在已经完成了手术,血值：%d，金钱：%d" % (renwu[1], xue_rmb[0], xue_rmb[1])
		print "%s: 如果你想复仇的话，建议你去%s找%s拜师学艺" % (renwu[2], difang[0], renwu[3])
		raw_input("按任意间继续")
		game_learn(game_name)
		
	elif "2" in xuanze_two or "不治疗" in xuanze_two:
		dead("由于你不愿治疗")	
	else:
		dead("用得着这么纠结吗？")
def start_game(game_name_temp):
	# 如果对全局变量进行修改，需要使用global进行声明
	global renwu
	renwu.append("火云邪神")
	renwu.append("系统提示")
	print "你是一个弱弱的少年，有一天放学，你走在路上，突然有几个人挡住了你的去路。"
	print "%s：喂，小子，直到我是谁吗？" % renwu[0]
	print "%s：并...并不知⊙﹏⊙" % game_name_temp
	print "%s：哇哈哈哈，我是当地赫赫有名的%s，小子，你保护费交了吗？" % (renwu[0], renwu[0])
	print "%s：我，我没钱，大哥饶了我吧|>_<|" % game_name_temp
	print "%s：没钱还敢在这学校混，那就受死吧╰_╯~" % renwu[0]
	
	global xue_rmb	
	xue_rmb[0] -= 80
	xue_rmb[1] -= 200
	print "%s：你被%s打败了，你现在的血值：%d，金钱：%d" % (renwu[1], renwu[0], xue_rmb[0], xue_rmb[1])
	while True:
		print """
		1. 君子报仇，十年不晚！立刻拨打120去医院救治.
		2. 是可忍孰不可忍，我要立刻找%s报仇！
		""" % renwu[0]
		xuanze_one = int(raw_input("你快要挂了，请键入数字做出选择："))
		if xuanze_one == 1:
			hospital_game()
		elif xuanze_one == 2:
			boss_game()
		else:
			print "只能输入”1“或”2“"	
			
		
start_game(game_name) 