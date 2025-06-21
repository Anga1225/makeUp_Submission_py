# function
def f(x):
    y = x * x
    return y
print("f(1) = " , f(1))
print("f(0) = " , f(0))
print("f(2) = " , f(2))

# 10-2
def Celsius_to_Fahrenheit(x):
    F = 9 / 5 * x + 32
    return F

t = eval(input("Please enter temperature in Celsius: "))
print("The temperature is: ", Celsius_to_Fahrenheit(t))

# 10-3
import math
def Cnk(n, k):
    coeff = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return int(coeff)

print("C(5, 3)", Cnk(5, 3))
print("C(5, 3)", Cnk(n= 5, k = 3))
print("C(5, 3)", Cnk(k = 3, n = 5))

# 10-4
def Cnk(n = 5, k = 3 ):
    coeff = math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
    return int(coeff)
print("C(5, 3)", Cnk())
print("C(6, 4)", Cnk(6, 4))

# 10-5
def f(x):
    y = x * x
    return y

# 10-6
def ff(x):
    x = x + 1
    print("The value of x in function is: ", x)

def main():
    # 10-5
    print("f(1) = ", f(1))
    print("f(0) = ", f(0))
    print("f(-1) = ", f(-1))

    # 10-6
    x = 1
    print("The value of x before function call is: ", x)
    f(x)
    print("The value of x after function call is: ", x)

# 10-7
def isPrime(n):
    for i in range(2, n//2 + 1):
        if n % i == 0:
            return False
    return True

number = eval(input("Please enter a positive number: "))

if isPrime(number):
    print("The entered number is Prime")
else:
    print("The entered number is Not Prime")

# 10-8
num_of_prime = 0
n = 2
while num_of_prime < 50:
    if isPrime(n):
        print(format(n, "4d"), end=" ")
        num_of_prime += 1
        if num_of_prime % 10 == 0:
            print()
    n += 1