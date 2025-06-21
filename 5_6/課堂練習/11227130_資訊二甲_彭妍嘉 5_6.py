# 11-1
def f(n):
    if n == 0:
        return 0
    else:
        return f(n - 1) + n

# 11-2
def Fib(n):
    if n == 0 or n == 1:
        return n
    return Fib(n - 1) + Fib(n - 2)

# 11-3
def Catalen(n):
    if n == 0:
        return 1
    else:
        sum = 0
        for k in range (0, n):
            sum += Catalen(k) * Catalen(n - k - 1)
        return sum

# 11-4
def Cnk(n, k):
    if n == 0 or n == k:
        return 1
    return Cnk(n - 1, k) + Cnk(n - 1, k - 1)

# 11-6
def gcd(a, b):
    if b == 0:
        return a;
    return gcd(b, a % b)


if __name__ == '__main__':
    print(f(100))
    for i in range(10):
        print("Fib(%d) = %d" % (i, Fib(i)))
    for n in range(10):
        print("Catalen(%d) = %d" % (n, Catalen(n)))
    print("C(5, 3) = ", Cnk(5, 3))
    print("C(4, 2) = ", Cnk(4, 2))
    print("C(4, 3) = ", Cnk(4, 3))
    # 11-5
    for n in range(10):
        for k in range(n + 1):
            print(Cnk(n, k), end = " ")
        print()
    a, b = eval(input("Please enter two numbers: "))
    ans = gcd(a, b)
    print("GCD(%d, %d) = %d" % (a, b, ans))

