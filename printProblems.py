"""
String Concatenation:
1.create a variable and assign it the phrase "hello world" by concatenating the strings "hello" and " world"
2.create a variable and assign it the integer 11
3.create a variable and assign it the integer 38
4.create a variable and use the variables from steps 2 and 3 and string concatenation to assign it the string
"1138"
"""
# type your code for "String Concatenation" below this comment and above the one below it.-----------------------------
myVariable = "hello" + "World"

int1 = 11
int2 = 38

Resultint = str(int1) + str(int2)


# ----------------------------------------------------------------------------------------------------------------------
"""
%s and input():
1.create a variable to hold a user's favorite restaurant (use input() for this.)
2.create a variable to hold the name of a place a user wants to visit.
3.create a variable to hold the user's nickname or first name if they don't have a nickname.
4.use the %s operator to assign the string "Your favorite restaurant is [name of favorite restaurant], you want
to visit
[name of place the user wants to visit], and your nickname or first name is [nickname or first name]" to a
variable
5.print that variable
"""
# type your code for "%s and input()" below this comment and above the one below it.-----------------------------------
Restaurant = input("What is you favorite restaurant")
Place = input("Which place you want to visit")
Name = input("What is your Nickname/Firstname")

Answer = "Your favorite restaurant is %s, you want to visit %s, and your Nickname is %s." % (Restaurant,Place,Name)
print(myVariable)
print(Resultint)
print(Answer)

# ----------------------------------------------------------------------------------------------------------------------