def R(r, n):
    if n == 0:
        return 1
    return r**n + R(r, n - 1)

if __name__ == '__main__':
    n, r = eval(input("Please enter two numbers n, r: "))
    ans = R(r, n)
    print(("sum = %d") % ans)

