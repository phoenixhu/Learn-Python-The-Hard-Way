# -*- coding: utf-8 -*-
# 你叫什么？
print "Please enter name:"
name = raw_input()
# 你是好人吗？
print "Are you a good person:"
person = raw_input()
# 你在什么地方？
print "where are you?",
where = raw_input()
# 你出生在哪一年？
year = input("What year were you born:")
print "My name is %s, is a %s, living in %s, %d years old" % (name, person, where, 2015 - year)
