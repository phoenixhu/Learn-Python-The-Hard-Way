# -*- coding: utf-8 -*-

from nose.tools import *

from ex47.game import Room

def test_room():
    # 将Room类实例化
    gold = Room("GoldRoom",
                """This room has gold in it you can grad. There's a
                door to the north.""")

    # 测试实例属性name是不是“GoldRoom”,如果不是将报异常
    assert_equal(gold.name, "GoldRoom")
    
    # 测试实例属性paths是不是字典，如果不是将报异常
    assert_equal(gold.paths, {})

def test_room_paths():
    
    # 将Room类实例化
    center = Room("Center", "Test room in the ceter.")

    north = Room("North", "Test room in the north.")

    south = Room("South", "Test room in the south.")

    # 将参数中的字典更新到paths字典中
    center.add_paths({'north': north, 'south': south})
    
    # 测试center实例中的go方法，查找north键并返回字典值，测试字典值是不是north实例对象返回值，否则报异常
    assert_equal(center.go('north'), north)
    
    # 测试center实例中的go方法，查找south键并返回字典值，测试字典值是不是south实例对象返回值，否则报异常
    assert_equal(center.go('south'), south)

def test_map():
    
    # 将Room实例化
    start = Room("Start", "You can go west and down a hole.")

    west = Room("Trees", "There are tress here here, you can go east.")

    down = Room("Dungeon", "It's dark down here, you can go up.")

    # 将参数中的字典更新到paths字典中
    start.add_paths({'west': west, 'down': down})
    
    # 将参数中的字典更新到paths字典中
    west.add_paths({'east': start})
    
    # 将参数中的字典更新到paths字典中    
    down.add_paths({'up': start})


    assert_equal(start.go('west'), west)

    assert_equal(start.go('west').go('east'), start)

    assert_equal(start.go('down').go('up'), start)
