# 9-1
i = 1
sum = 0
while i <= 100:
    sum += i
    i += 1
print(sum)

# 9-2
i = 1
sum = 0
while True:
    sum += i
    if i == 100:
        break
    i += 1
print(sum)

# 9-3
i = 0
while i <= 10:
    i += 1
    if i % 2 == 0:
        continue
    print(i)

# 9-4
sum = 0
for i in range(1, 101):
    sum += i
print(sum)

# 9-5
for i in range(10):
    for j in range(10):
        print("Hello!")
# 9-6
import random
num = random.randint(1, 100)

while True:
    guess = eval(input("Guess a number between 1 and 100: "))
    if guess == num:
        print("Bingo")
        break
    if guess < num:
        print("Guess higher")
    else:
        print("Guess lower")

# 9-7
n = eval(input("Enter a number: "))
sum = 0
r = 0.5
for k in range(n):
    sum += r**k
print("Sum = ", sum)

# 9-8
number = eval(input("Enter a number: "))

for n in range(1, number + 1):
    print("2**" + str(n) + " = " + str(2**n))

# 9-9
import math
number = eval(input("Enter a number of n!: "))
for n in range(1, number + 1):
    print(str(n) + "! = " + str(math.factorial(n)))

# 9-10
n = eval(input("Enter a number: "))

for i in range(1, n + 1):
    print(" " * (n-i), end = "")
    print("*" * (2 * i - 1))

# 9-11
a, b = eval(input("Enter two numbers a, b: "))
gcd = 1
for k in range(2, min(a, b) + 1):
    if a % k == 0 and b % k == 0:
        if k > gcd:
            gcd = k
if gcd != 1:
    print("GCD = " + gcd)
else:
    print("No GCD")

# 9-12
print(" |", end = '')
for j in range(2, 10):
    print(" ", j, end = ' ')
print()
print("----------------------------------")
for i in range(2, 10):
    print(i, "|", end = ' ')
    for j in range(2, 10):
        print(format(i * j, '4d'), end = '')
    print()
