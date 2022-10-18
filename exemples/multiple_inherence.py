class A:
    def __init__(self,p,r):
        self.p=p
        self.r=r

class B:
    def __init__(self,h):
        self.h=h

class C(A,B):
    def __init__(self,x,y):
        super().__init__(1,2)
        self.x=x
        self.y=y
Test=C(5,10)
print(Test.x)
print(Test.p)
print(Test.r)
#print(Test.h)
print(Test)
print(dir(Test))
