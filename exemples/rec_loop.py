def F(n):
	p1=1
	p2=1
	for i in range(3,n+1):
		p1,p2=p2,p1+p2
	return p2

def Factorial(n):
	p=1
	for i in range(2,n+1):
		p*=i 
	return p

print(Factorial(5))
print(F(6))