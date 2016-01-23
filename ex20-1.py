from sys import argv
script, filename = argv
def test_one(s):
	print s.read()
def test_two(q):
	q.seek(0)
def test_three(ss, e):
	print ss, e.readline(),	
a = open(filename)
test_one(a)	
test_two(a)
number1 = 0
number2 = 1
number1 += number2
test_three(number1, a)
number1 += number2
test_three(number1, a)
number1 += number2
test_three(number1, a)
