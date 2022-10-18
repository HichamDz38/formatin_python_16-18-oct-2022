for i in range(2,100): 
	for j in range(2,int(i**0.5)+1): 
		if i%j==0: 
			break 
		if (j >= int(i**0.5)) : 
			print(i)

