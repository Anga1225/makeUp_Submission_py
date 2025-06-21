def F_to_C(x):
    C = 5 / 9 * (x - 32)
    return round(C, 1)

t = eval(input("Please enter temperature in Fahrenheit: "))
print("The temperature is: ", F_to_C(t))