import math
print(dir(math)) # to see all available functions
degree=int(input("enter the degree: ")) # the value is module 360
degree/=360
degree*=math.pi*2
print(degree)
value=math.cos(degree)
print(value)