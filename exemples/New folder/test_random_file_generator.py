import random



name = "".join([chr(random.randint(65,92)) for i in range(random.randint(5,10))])+".txt"
open(name, "a")