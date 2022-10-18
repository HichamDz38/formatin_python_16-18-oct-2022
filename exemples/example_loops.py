List = [1,2,3,4,-5,-1,100,2,5,7,4111]
List2 = [1,2,3,4,-5,-1,100,2,5,7,4111]

for e in List:
    print(e)
    e = e+2
    print(e)

print(List)

for i in range(len(List)):
    if List[i]<0 :
        List[i] =  abs(List[i])
print(List)


from random import randint

magic = randint(0, 5)

v = magic*2
while v!= magic:
    v = int(input('enter a number : '))
    if v > magic:
        print("plus grand")
    elif v<magic :
        print("plus petit")
    else:
        print("correct")
    
    


