n = eval(input("Enter a number: "))

for i in range(1, n + 1):
    print(" " * (i), end = "")
    print("*" * (2 * n - (i * 2 - 1)), end = "")
    print()


