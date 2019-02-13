"""
1.Iterating through a string using range() and a for loop
a.create a string and assign it to a variable
b.use a for loop without a range() to iterate through and print the contents of the string from step 1.a.
c.use a for loop with a range() to iterate through and print the contents of the string from step 1.a.
"""
#----------------------------------------------------------------------------------------------------
myStringVar = "implementation"
for char in myStringVar:
    print(char)

for char in range(len(myStringVar)):
    print(myStringVar[char])

#-----------------------------------------------------------------------------------------------------
"""
2.Using , and end to print output of a for loop on the same line
a.create a variable and assign it a list of integers
b.use a for loop with , and end to print all the integers from the list you made as one integer (eg if your list was
[1, 2, 5, 7], the output of the for loop should be 1257)
c.use a for loop with , and end to print all the integers from the list you made with "X" between them (eg if your list
was [4, 3, 2, 1], the output of the for loop should be 4X3X2X1X)
"""
#----------------------------------------------------------------------------------------------------
myStringVar1 = [1,2,3,4,5]
for char in myStringVar1:
    print(char,end="")

print("")
for char1 in myStringVar1:
    print(char1,end="X")

#----------------------------------------------------------------------------------------------------
"""
3.Using a for loop to iterate through a dictionary
a.create a dictionary and assign it to a variable
b.use a for loop to iterate through the dictionary and print its keys and values with the following form:
value key (eg, if your dictionary is {"first": 1, "second": 2}, your output should be 1 "first" and on another line
2 "second")(since dictionaries don't have to print in order, your output with {"first": 1, "second": 2} as your
dictionary could have also been 2 "second" and on another line 1 "first")
"""
#----------------------------------------------------------------------------------------------------
print("")
myDict = {12:"Hey",23:"There",22:"You"}
for keys in myDict:
    print(str(keys) +" "+ myDict[keys])
#-----------------------------------------------------------------------------------------------------
"""
4.zip()
a.create 2 lists of numbers and assign them to variables
b.use a for loop and zip() to iterate through both those lists, sum their values, and append those values to a new list
(eg, if one of your lists is [1, 2] and your other list is [5, 9], then the for loop would iterate through them,
add 1 to 5 resulting in 6 and add 2 to 9 resulting in 11)
c.print the new list (the resulting list from the example given in 4.b. would be [6, 11])
"""
#---------------------------------------------------------------------------------------------------------
list1 = [2,4,1,11]
list2 = [12,33,43,2]
list3 = []
for item1,item2 in zip(list1,list2):
    result = item1 + item2
    list3.append(result)

print(list3)
#---------------------------------------------------------------------------------------------------------
"""
5.for/else
a.create a tuple with 5 elements that are all strings and assign it to a variable
b.create a for/else loop that prints the first 4 elements of the tuple from step 5.a. with its for loop portion and
the fifth element of the tuple from step 5.a. with the else statement
c.create a for/else loop that prints the first 3 elements of the tuple from step 5 then ends prematurely before the else
statement is triggered using a break statement
"""
mytup = ("HEy","There","Man","Hows","You")
for items in mytup:
    if True:
        print(*range(0,len(mytup)))
# TO be Worked on......



