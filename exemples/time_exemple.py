import time

print(dir(time))
time.sleep(5)           #block the flow with 5 seconds
print(time.strftime("%H"))     # get the actual hour
print(time.strftime("%Y"))    # get the actual year
print(time.strftime("%y"))     # get the actual year modulo 100
print(time.strftime('%D'))     # get the actual month/day/year%100
print(time.strftime('%h'))     # get the actual month/day/year%100
print(time.strftime())     # get the actual month/day/year%100
print(time.strftime("%Y-%M-%d %H:%M:%S"))  #get the actual timestamp