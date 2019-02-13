myListofInt = [21,22,1,33,45,60]
def myfunc1(list1):
    for items in list1:
        print(items)

myfunc1(myListofInt)

myRangeList = range(10)
myRangeList1 = range(4,8)
myRangeList2 = range(5,21,5)

#print(*myRangeList2) * to unpack results

def myfunc2(a):
    return a

print(*myfunc2(myRangeList))

def myfunc3(a):
    for elements in a:
        print(elements)

myfunc3(myRangeList1)


def myfunc4(a):
    for items in a:
        items+=3
        print(items)

myfunc4(myRangeList2)

def myfunc5(a,b):
    print(a,b)

print(myfunc5(myfunc4(myRangeList2),myRangeList2))

print(*myRangeList2)



listoflists = [["ameya","pandey"],["anurag","deshpandey"],["Dinesh","Mukhi"]]

def myfunc6(a):
    empty = []
    for items in a:
        for elements in items:
            empty.append(elements)
            print(empty)



myfunc6(listoflists)


