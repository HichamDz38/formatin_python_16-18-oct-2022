import re

email1 = "hicham@gmail.com";
email2 = "hichamgmail.com";
email3 = "hicham@gmailcom";

result1 =re.search('^[a-z A-Z]*@*.*',email1)
print(result1.group(0))
result2 =re.search('^[a-z A-Z]*@*.*',email2)
print(result2.group(0))
result3 =re.search('^[a-z A-Z]*@*.*',email3)
print(result3.group(0))