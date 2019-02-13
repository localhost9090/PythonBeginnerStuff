"""
1.Basic List Comprehensions
a.use a basic list comprehension to generate and print the list [8, 6, 4, 2, 0]
b.use a basic list comprehension to generate and print the list [1, 4, 27, 256]
c.use a basic list comprehension to generate and print the list [24, 35, 48]
2.List Comprehensions with If Statements
a.use a list comprehension with an if statement to generate and print the list [2, 3, 4, 7, 8, 9]
b.use a list comprehension with an if statement to generate and print the list [10, 9, 8, 3, 2, 1]
c.use a list comprehension with an if statement to generate and print the list [1, 4, 5, 6, 9, 10]
"""
listcomp = [item*2 for item in range(0,5)]
listcomp.reverse()
print(listcomp)
listcomp1 = [item1**item1 for item1 in range(1,5)]
print(listcomp1)
listcomp2 = [item2**2-1 for item2 in range(5,8)]
print(listcomp2)





secondlist = [element for element in range(2,10) if element%5!=0 and element!=6]
print(secondlist)

secondlist1 = [element1 for element1 in range(1,11) if element1!=6 and element1!=7 and element1!=5 and element1!=4]
secondlist1.reverse()
print(secondlist1)

