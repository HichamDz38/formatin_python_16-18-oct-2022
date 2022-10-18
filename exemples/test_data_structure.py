# this is comment

""""
this is a multi line comment
"""
from cmath import sqrt
from dis import Instruction
from symbol import decorator


_var1, var2 = 12, 144
X = 1, 2, 3
print(_var1, var2)
print(X)

# tester les data types
chain =  "chainedecdqfq"
chain3 = "123456789"
chain2 = """
another String in multi
lines
"""

print(chain)
print(chain2)

print(chain[::-1])
print(chain2[::-1])

Z = zip(chain, chain3)
print(list(Z))

D = dict(Z)
print(D)

print(type(Z),type(chain),)

S = set(chain)
print(S)
print(len(S))
D["key"] = "value"
print(len(D))

"""

if True :
    print("Ture value")
    print("Ture value")
    print("Ture value")

if len(input("enter a tall chain"))>5 :
    print("Ture value")
    print("Ture value")
    print("Ture value")
"""

#X = int(input("enter a positive number : "))
L = []
if X or []: # the value of X is -5
    print("True value")
else:
    print("False value")
# les valeurs fause et les valuers True

def name_of_the_funcion(x, y, z=100):
    if not(x.isdigit()) or not(y.isdigit()):
        return False
    return int(x)+int(y)+z


y = lambda x,y,z:x*y*z

print(y(5,2,3))
print(name_of_the_funcion("123","123", 300))



    
def funtion2(funct):
    a, b ,c = [], [], []
    def manipulation():
        print("#"*40)
        print("#"*40)
        funct(c)
        print("#"*40)
        print("#"*40)
    return manipulation

@funtion2
def function(arg = []):
    arg.append(4)
    print(arg)


function() 


for i in [1, 2, 3 , 4 , 5]:
    print(i)


git clone https://github.com/HichamDz38/formatin_python_16-18-oct-2022

for i in "Hello World":
    print(i)

L = "Hello"
for i in range(len(L)):
    print(L[i])
    

for i in range(10):
    print(i, end= "  ")
    

