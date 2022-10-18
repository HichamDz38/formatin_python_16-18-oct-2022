n=int(input())
d={}
e=2
while e<=n:
	print(e,d)
	d[e]=e**2
	e+=2
	print(e,d)
print(d)