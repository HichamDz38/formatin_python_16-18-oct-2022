i = 2 
while(i < 100): 
	j = 2 
	while(j <= i**0.5): 
		if i%j==0: 
			continue 
			print('continue')
		print('not continue')
		
		if (j > i**0.5) : 
			print(i)
	i = i + 1  
