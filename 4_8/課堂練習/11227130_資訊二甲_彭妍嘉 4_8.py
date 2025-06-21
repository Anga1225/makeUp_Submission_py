# Please enter 2 num
from numba.np.npdatetime import is_leap_year

a, b = eval(input("Please enter two numbers: "))

if a < b:
    print(a, "<", b)

# Please enter 2 num
a, b = eval(input("Please enter two numbers: "))

if a <= b:
    print(a, "<=", b)
else:
    print(b, "<", a)

# Please enter score
score = eval(input("Please enter score: "))

if score >= 90:
    print("Grade = A")
elif score >= 80:
    print("Grade = B")
elif score >= 70:
    print("Grade = C")
elif score >= 60:
    print("Grade = D")
else:
    print("Grade = F")

# 請輸入西元年份
year = eval(input("Please enter year: "))
zodiacYear = year % 12
if zodiacYear == 0:
    print("猴年")
elif zodiacYear == 1:
    print("雞年")
elif zodiacYear == 2:
    print("狗年")
elif zodiacYear == 3:
    print("豬年")
elif zodiacYear == 4:
    print("鼠年")
elif zodiacYear == 5:
    print("牛年")
elif zodiacYear == 6:
    print("虎年")
elif zodiacYear == 7:
    print("兔年")
elif zodiacYear == 8:
    print("龍年")
elif zodiacYear == 9:
    print("蛇年")
elif zodiacYear == 10:
    print("馬年")
else:
    print("羊年")

# Leap Year
year = eval(input("Please enter year: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    isLeapYear = True
else:
    isLeapYear = False

if isLeapYear:
    print(str(year) + "是閏年")
else:
    print(str(year) + "不是閏年")

# BMI
height = eval(input("Please enter height(cm): "))
weight = eval(input("Please enter weight(kg): "))

height /= 100
BMI = weight / (height * height)

if BMI < 18.5:
    print("過輕")
elif BMI < 25:
    print("適中")
elif BMI < 30:
    print("過重")
else:
    print("肥胖")
