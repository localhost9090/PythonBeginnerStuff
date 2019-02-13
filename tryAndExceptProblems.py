"""
1.Try and Except to handle divide by zero and type errors
a.Use input() to have the user enter two integers as inputs. Assign these to 2 different variables.
b.Define a function that takes two inputs. This function should print the result of the first input divided by the
second input. Use your knowledge of Try and Except statements to print messages for the errors that would occur if
the
second input of the function is 0 or if one or both of the inputs cannot be converted to integers.
c.call the function from step 1.b. with the 2 variables from step 1.a. as inputs.
"""

value1 = input("Please enter first number")
value2 = input("Please enter second number")
int1 = int(value1)
int2 = int(value2)
def divide(first,second):
    try:
        result = first/second
        print(str(result))

    except ZeroDivisionError:
        print("Cannot Divide by Zero")

divide(int1,int2)