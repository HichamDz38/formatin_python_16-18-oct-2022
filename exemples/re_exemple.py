import re

print(dir(re))

txt = "The rain in Spain"
x  =  re.findall("ai", txt)
x2 = re.sub("ai",'ia',txt)
x3 = re.split("ai",txt)   # it's like the str split but take a re instead of one char
x4 = re.split("[.,;:]","1,2,3;4:5.6")   # it's like the str split but take a re instead of one char
x5 = re.split("[,;:]","1,2,3;4:5.6")   # it's like the str split but take a re instead of one char
x6 = re.sub("[;:]",",","1,2,3;4:5.6")
x7 = list(map(eval,re.sub("[;:]",",","1,2,3;4:5.6").split(',')))
print(x)
print(x2)
print(x3)
print(x4)
print(x5)
print(x6)
print(x7)