import math as m
# print name
name = input("請輸入姓名： \n")
print("Hello! " + name)

# practice eval
print(eval("113.132"))
print(eval("123 * 3"))
print(eval("123 + 3"))
print(eval("4 ** 3"))

# pratice coveting user input into number
radius = eval(input("請輸入半徑： "))
area = m.pi * radius ** 2
print(area)

# input a & b at once
a = eval(input("Please input num a: \n"))
b = eval(input("Please input num b: \n"))
print("a =", a)
print("b = ", b)

# input 3 num at once
a, b, c = map(float, input("Please enter 3 numbers separated by spaces: ").split())
average = (a + b + c) / 3
print("Average:", average)

# cat the string
print("Hello " + "Anga")
print("Hello ", "Bob")
print("Hello ", "Bob", end = "~~~~")
# non printable
print("Hello world\n")
print("Hello world\t")
print("\"Hello world\"")

# round
print(round(m.pi, 5))
print(round(m.e, 6))
x = 4
y = 6
z = 6 ** 4
print(format(x, "5d"))
print(format(z, "10d"))

print(format(m.pi, "4.4f"))
print(format(m.pi, "4.4e"))
print(format(134134.13242, "4.4e"))
print(format(12312, "4.4e"))

# format output
x = 10000
print("x = %d" % x)
print("x = %5d" % x )
print("x = %e" % x)
print("x = %.2f"  % m.pi)
print("x = %5.4f" % m.e)
print("x = %o (oct)" %x)
print("x = %x (hex)" %x )
print("x = %s" % str(231.134))

# read file
infile = open("text.txt", "r")
print(infile.read())
infile.close()

infile = open("text.txt", "r")
print(infile.readlines())
infile.close()

# write file
outfile = open("text.txt", "w")
outfile.write("Hello world\n")
outfile.close()

