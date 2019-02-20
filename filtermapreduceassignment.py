from functools import reduce

number = [23,56,12,22,45,74,111]
#Filter Function
odd = list(filter(lambda a:a%2!=0 , number))
print(odd)

#Map Function
func = list(map(lambda a:a-1 ,odd))
print(func)

#Filter Function
mul = reduce(lambda a,b:a*b , func)
print(mul)