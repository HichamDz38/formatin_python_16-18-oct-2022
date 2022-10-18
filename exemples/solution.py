List=[90,[50,[20,[5],[25]],[75,[66],[80]]],[150,[95,[92],[111]],[175,[166],[200]]]]

def print_list(Li):
	#print("this is the input: ",Li)
	if len(Li)==3:
		return Li[0]+min(print_list(Li[1]),print_list(Li[2]))
	else:
		return Li[0]

print(print_list(List))