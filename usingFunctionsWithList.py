"""
0.Setup:
a.create a list of integers and assign it to a variable
b.create a list of strings and assign it to a variable
c.create a list of floats and assign it to a variable
1.Passing A List to A Function:
a.create a function that takes and returns an input
b.print a call of the function you created in step 1.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 1.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 1.a. with the list of floats from step 0.c. as the input
2.Accessing An Element In A list using A Function:
a.create a function that takes a list as an input and returns one of that lists elements
b.print a call of the function you created in step 2.a. with the list of integers from step 0.a. as the input
c.print a call of the function you created in step 2.a. with the list of strings from step 0.b. as the input
d.print a call of the function you created in step 2.a. with the list of floats from step 0.c. as the input
3.Modifying A List Element Within A Function:
a.create and call a function that prints the product of all the integers from the list you created in step 0.a.
b.create and call a function that concatenates all the strings from the list you create in step 0.b and prints the
result
c.create and call a function that prints the quotient of all the floats from the list you created in step 0.c.
4.Manipulating Lists Within Functions:
a.create a list that uses 3 of the following functions on one of the lists you created in part 0 of this problem set:
.index(), .append(), .remove(), .insert, or .pop(). Also, make sure that the function prints the resulting list
b.call the function from part 4.a. using one of the lists you made in part 0 of this problem set.
"""
myListInt = [12,23,5,6]
myListString = ["Pratik","Anurag","Dinesh"]
myListFloat = [2.1,3.5,7.9]

def myfunc(input):
    return input

print(myfunc(myListInt))
print(myfunc(myListString))
print(myfunc(myListFloat))


def prodfunc(list1):
    return list1[0]*list1[1]*list1[2]*list1[3]


print(prodfunc(myListInt))


def concatstr(list2):
    return list2[0] + list2[1] + list2[2]

print(concatstr(myListString))

def func(list3):
    list3.append(7)
    list3.remove(12)
    list3.insert(1,66)
    list3.pop(3)
    return list3

print(func(myListInt))