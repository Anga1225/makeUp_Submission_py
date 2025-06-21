import random

n = eval(input("Please enter the number: "))
list = [random.randint(1, 100) for i in range(n)]
print(list)