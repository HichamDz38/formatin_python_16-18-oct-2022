# how to create a generate of prime number from 2 to 100

# the first way to create a generator
from os import execv


G1 = (i for i in range(2,101))
N = next(G1)
while N:
    print(N, end = " ")
    try:
        N = next(G1)
    except:
        break

def generator():
    for i in range(2, 101):
        yield i
G2 = generator()
print('='*100)
N = next(G2)
while N:
    print(N, end = " ")
    try:
        N = next(G2)
    except:
        break

