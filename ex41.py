# -*- coding: utf-8 -*-

# 导入exit成员，用作程序退出
from sys import exit 
# 导入randint成员，用作随机生成数字
from random import randint  

# 定义death函数
def death(): 
    # 生成一个列表
    quips = ["You died.  You kinda suck at this.", 
             "Nice job, you died ...jackass.", 
             "Such a luser.", 
             "I have a small puppy that's better at this."] 
   # 打印列表的某个索引值的元素，索引值通过randint()函数随机生成，随机生成的数字范围是0-3
    print quips[randint(0, len(quips)-1)] 
   # 异常退出 
    exit(1)   

# 定义central_corridor函数，开始游戏
def central_corridor(): 
    '''
    The Gothons of Planet Percal #25 have invaded your ship and destroyed
    your entire crew.  You are the last surviving member and your last
    mission is to get the neutron destruct bomb from the Weapons Armory,
    put it in the bridge, and blow the ship up after getting into an
    escape pod.
    \n
    You're running down the central corridor to the Weapons Armory when
    a Gothon jumps out, red scaly skin, dark grimy teeth, and evil clown costume
    flowing around his hate filled body.  He's blocking the door to the
    Armory and about to pull a weapon to blast you.
    '''
    # 提示用户输入
    action = raw_input("> ")  
    # 如果用户输入的是shoot!执行语句块代码
    if action == "shoot!": 
        print "Quick on the draw you yank out your blaster and fire it at the Gothon." 
        print "His clown costume is flowing and moving around his body, which throws"			 
        print "off your aim.  Your laser hits his costume but misses him entirely.  This" 
        print "completely ruins his brand new costume his mother bought him, which" 
        print "makes him fly into an insane rage and blast you repeatedly in the face until" 
        print "you are dead.  Then he eats you." 
        # 将此字符串返回
        return 'death'  
    
    # 如果用户输入的是dodge!执行语句块代码
    elif action == "dodge!": 
        print "Like a world class boxer you dodge, weave, slip and slide right" 
        print "as the Gothon's blaster cranks a laser past your head." 
        print "In the middle of your artful dodge your foot slips and you" 
        print "bang your head on the metal wall and pass out." 
        print "You wake up shortly after only to die as the Gothon stomps on" 
        print "your head and eats you." 
        # 将此字符串返回    
        return 'death'  
    
    # 如果用户输入的是tell a joke执行语句块代码
    elif action == "tell a joke": 
        print "Lucky for you they made you learn Gothon insults in the academy." 
        print "You tell the one Gothon joke you know:" 
        print "Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr, fur fvgf nebhaq gur ubhfr." 
        print "The Gothon stops, tries not to laugh, then busts out laughing and can't move." 
        print "While he's laughing you run up and shoot him square in the head" 
        print "putting him down, then jump through the Weapon Armory door." 
        # 将此字符串返回
        return 'laser_weapon_armory'  
    # 如果以上判断都不是，执行语句块代码
    else: 
        print "DOES NOT COMPUTE!" 
        # 将此字符串返回
        return 'central_corridor'  
    
# 定义函数    
def laser_weapon_armory(): 
    '''
    You do a dive roll into the Weapon Armory, crouch and scan the room 
    for more Gothons that might be hiding.  It's dead quiet, too quiet. 
    You stand up and run to the far side of the room and find the 
    neutron bomb in its container.  There's a keypad lock on the box 
    and you need the code to get the bomb out.  If you get the code 
    wrong 10 times then the lock closes forever and you can't 
    get the bomb.  The code is 3 digits. 
    '''
    # 生成三组随机数字1-9
    code = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9)) 
    
    # 用户输入
    guess = raw_input("[keypad]> ") 		
    # 定义初始变量默认值0
    guesses = 0  
    # 表达式成立，为True，开始循环，直到表达式为Flase退出循环
    while guess != code and guesses < 10: 
        # 打印字符串
        print "BZZZZEDDD!" 
        # guesses在原值上加1
        guesses += 1 
        # 用户再次输入，得到新的字符串
        guess = raw_input("[keypad]> ")  
    
    # 如果用户输入的值等于随机生成的值，执行语句块代码
    if guess == code: 
        print "The container clicks open and the seal breaks, letting gas out." 
        print "You grab the neutron bomb and run as fast as you can to the" 
        print "bridge where you must place it in the right spot." 
       # 将此字符串返回
        return 'the_bridge'
    
    # 如果不是，执行语句块代码
    else: 
        print "The lock buzzes one last time and then you hear a sickening" 
        print "melting sound as the mechanism is fused together." 
        print "You decide to sit there, and finally the Gothons blow up the" 
        print "ship from their ship and you die." 
        # 将此字符串返回
        return 'death'   

# 定义函数
def the_bridge(): 
    '''
    You burst onto the Bridge with the neutron destruct bomb 
    under your arm and surprise 5 Gothons who are trying to 
    take control of the ship.  Each of them has an even uglier 
    clown costume than the last.  They haven't pulled their 
    weapons out yet, as they see the active bomb under your 
    arm and don't want to set it off. 
    '''
     
    # 用户输入
    action = raw_input("> ")  
    # 如果用户输入是表达式的字符串，执行语句块代码
    if action == "throw the bomb": 
        print "In a panic you throw the bomb at the group of Gothons" 
        print "and make a leap for the door.  Right as you drop it a" 
        print "Gothon shoots you right in the back killing you." 
        print "As you die you see another Gothon frantically try to disarm" 
        print "the bomb. You die knowing they will probably blow up when" 
        print "it goes off." 
        # 将此字符串返回
        return 'death'  
    
    # 如果用户输入是表达式的字符串，执行语句块代码
    elif action == "slowly place the bomb": 
        print "You point your blaster at the bomb under yourarm" 	
        print "and the Gothons put their hands up and start to sweat." 
        print "You inch backward to the door, open it, and then carefully" 
        print "place the bomb on the floor, pointing your blaster at it." 
        print "You then jump back through the door, punch the close button" 
        print "and blast the lock so the Gothons can't get out." 
        print "Now that the bomb is placed you run to the escape pod to" 
        print "get off this tin can." 
        # 将此字符串返回
        return 'escape_pod' 
    
    #如果以上都不是，执行语句块代码
    else: 
        print "DOES NOT COMPUTE!" 
        return "the_bridge"  

# 定义函数
def escape_pod(): 
    '''
    You rush through the ship desperately trying to make it to 
    the escape pod before the whole ship explodes.  It seems like 
    hardly any Gothons are on the ship, so your run is clear of 
    interference.  You get to the chamber with the escape pods, and 
    now need to pick one to take.  Some of them could be damaged 
    but you don't have time to look.  There's 5 pods, which one 
    do you take?  
    '''
    # 生成数字，范围1-5
    good_pod = randint(1,5) 
    # 用户输入
    guess = raw_input("[pod #]> ")   
    # 比对，现将用户输入的值转换成整型，如果用户值不等于随机生成的数字，执行语句块代码
    if int(guess) != good_pod: 
        print "You jump into pod %s and hit the eject button." % guess 
        print "The pod escapes out into the void of space, then" 
        print "implodes as the hull ruptures, crushing your body" 
        print "into jam jelly." 
        # 将此字符串返回
        return 'death' 
    
    # 否则执行语句块代码
    else: 
        print "You jump into pod %s and hit the eject button." % guess 
        print "The pod easily slides out into space heading to" 
        print "the planet below.  As it flies to the planet, you look" 
        print "back and see your ship implode then explode like a" 
        print "bright star, taking out the Gothon ship at the same" 
        print "time.  You won!" 
        # 正常退出程序
        exit(0)   

# 生成一个字典
ROOMS = { 
    'death': death, 
    'central_corridor': central_corridor, 
    'laser_weapon_armory': laser_weapon_armory, 
    'the_bridge': the_bridge, 
    'escape_pod': escape_pod 
}   

# 定义函数，map是字典，strat是字典键
def runner(map, start): 
    # 将开始游戏函数赋给next变量
    next = start  
    # 进入无限循环
    while True: 
        # 先查找字典中开始游戏函数键的值，赋给room变量
        room = map[next] 
        # 打印字符串字符串
        print "\n--------" 
        # 打印函数注释
        print room.__doc__
        # 运行room()函数并将函数返回值赋给next变量
        next = room()  
runner(ROOMS, 'central_corridor')