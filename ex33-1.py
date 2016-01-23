def while_one(n, f, t, list):
    while n < f:
        print "At the top i is %d" % n
        list.append(n)
        
        n = n + t
        print "Numbers now: ", list
        print "At the bottom i is %d" % n
i1 = 0
i2 = 100
numbers = []

while_one(i1, i2, 2, numbers)

print "The numbers: "

for num in numbers:
    print num
        