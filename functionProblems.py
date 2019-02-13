"""
Single parameter and zero parameter functions:
1.define a function that takes no parameters and prints a string
2.create a variable and assign it the value 5
3.create a function that takes a single parameter and prints it
4.call the function you created in step 1
5.call the function you created in step 3 with the variable you made in step 2 as its input
"""
# ----------------------------------------------------------------------------------------------------------------------
def nopara():
    print("function with no parameters")


def onepara(a):
    print(a)



nopara()
onepara(5)




# ----------------------------------------------------------------------------------------------------------------------
"""
multiple parameter functions:
1.create 3 variables and assign integer values to them
2.define a function that prints the difference of 2 parameters
3.define a function that prints the product of the 3 variables
4.call the function you made in step 2 using 2 of the variables you made for step 1
5.call the function you made in step 3 using the 3 variables you created for step 1
"""
# ----------------------------------------------------------------------------------------------------------------------
def diff(firstVariable,secondVariable):
    output = firstVariable - secondVariable
    print(output)

def product(firstVariable,secondVariable,thirdVariable):
    result = firstVariable * secondVariable * thirdVariable
    print(result)


diff(5,9)
product(34,11,89)
# ----------------------------------------------------------------------------------------------------------------------
"""
Calling previously defined functions within functions:
1.create 3 variables and assign float values to them
2.create a function that returns the quotient of 2 parameters
3.create a function that returns the quotient of what is returned by the function from the second step and a
third
parameter
4.call the function you made in step 2 using 2 of the variables you created in step 1. Assign this to a
variable.
5.print the variable you made in step 4
6.print a call of the function you made in step 3 using the 3 variables you created in step 1
"""
# ----------------------------------------------------------------------------------------------------------------------
floatVal1 = 6.87
floatVal2 = 7.11
floatVal3 = 3.14

def quot():
    quotient = floatVal1/floatVal2
    return quotient


def quot1():
    newresult = quot()/floatVal3
    return newresult


myVariable = quot()
print(myVariable)

print(quot1())

# ----------------------------------------------------------------------------------------------------------------------
