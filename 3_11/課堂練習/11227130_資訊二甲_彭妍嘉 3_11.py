print("=== Python 基本資料型態 ===")

print("\n1. 整數型態:")
x = 3
print(f"x = {x}")
print(f"type(x) = {type(x)}")

print("\n2. 浮點數型態:")
y = 2.5
print(f"y = {y}")
print(f"type(y) = {type(y)}")

print("\n3. 複數型態:")
z1 = 1 + 2j
print(f"z1 = {z1}")
print(f"type(z1) = {type(z1)}")

z2 = complex(1, 2)
print(f"z2 = {z2}")
print(f"type(z2) = {type(z2)}")

print("\n4. 布林值型態:")
bool_true = True
print(f"bool_true = {bool_true}")
print(f"type(bool_true) = {type(bool_true)}")

bool_false = False
print(f"bool_false = {bool_false}")
print(f"type(bool_false) = {type(bool_false)}")

print("\n5. 字串型態:")
str1 = "Hello"
print(f'str1 = "{str1}"')
print(f"type(str1) = {type(str1)}")

str2 = "你好"
print(f'str2 = "{str2}"')
print(f"type(str2) = {type(str2)}")

print("\n=== 資料型態轉換 ===")

print(f"float(1) = {float(1)}")
print(f"int(3.1) = {int(3.1)}")
print(f"int(3.6) = {int(3.6)}")

print(f"bool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")
print(f"bool(1.0) = {bool(1.0)}")
print(f"bool(0.0) = {bool(0.0)}")

print(f"str(100) = '{str(100)}'")
print(f"str(3.1416) = '{str(3.1416)}'")

print("\n=== 變數記憶體位址 ===")
x = 1
y = 2
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")

print("\n=== 基本數學運算 ===")
print(f"2 + 3 = {2 + 3}")
print(f"10 - 3 = {10 - 3}")
print(f"3 * 4 = {3 * 4}")
print(f"1 / 10 = {1 / 10}")
print(f"123 / 999 = {123 / 999}")
print(f"100 // 3 = {100 // 3}")
print(f"100 % 3 = {100 % 3}")
print(f"2 ** 5 = {2 ** 5}")

print("\n=== 指定運算子 ===")
x = 1
print(f"初始 x = {x}")

x += 1
print(f"x += 1 後，x = {x}")

x *= 2
print(f"x *= 2 後，x = {x}")

y = 7
y //= 2
print(f"y = 7, y //= 2 後，y = {y}")

z = 100
z %= 3
print(f"z = 100, z %= 3 後，z = {z}")

print("\n=== 變數交換 ===")
x, y = 1, 2
print(f"交換前: x = {x}, y = {y}")

temp = x
x = y
y = temp
print(f"交換後: x = {x}, y = {y}")

x, y = y, x
print(f"再次交換: x = {x}, y = {y}")

print("\n=== 字串比較 (ASCII碼) ===")
print(f'"A" > "a" = {"A" > "a"}')
print(f'"A" < "a" = {"A" < "a"}')
print(f'"A" == "a" = {"A" == "a"}')
print(f'"A" != "a" = {"A" != "a"}')
print(f'"Apple" == "Orange" = {"Apple" == "Orange"}')
print(f'"Apple" != "Orange" = {"Apple" != "Orange"}')

print("\n=== 邏輯運算子 ===")
print(f"True and False = {True and False}")
print(f"True or False = {True or False}")
print(f"not True = {not True}")
print(f"not False = {not False}")

print(f"(5 > 3) and (2 < 4) = {(5 > 3) and (2 < 4)}")
print(f"(5 > 3) or (2 > 4) = {(5 > 3) or (2 > 4)}")
print(f"not (5 > 3) = {not (5 > 3)}")

print("\n=== 德摩根定律 (De Morgan's Law) ===")
print("not (p and q) 等價於 (not p) or (not q)")
print("not (p or q) 等價於 (not p) and (not q)")

x = True
y = True
print(f"\n當 x = {x}, y = {y} 時:")
print(f"not (x and y) = {not (x and y)}")
print(f"(not x) or (not y) = {(not x) or (not y)}")

x = False
y = False
print(f"\n當 x = {x}, y = {y} 時:")
print(f"not (x or y) = {not (x or y)}")
print(f"(not x) and (not y) = {(not x) and (not y)}")

print("\n=== 位元運算子 ===")
x = 6
y = 10

print(f"x = {x} (二進位: {bin(x)})")
print(f"y = {y} (二進位: {bin(y)})")

print(f"~x = {~x} (位元 NOT 運算)")
print(f"x & y = {x & y} (位元 AND 運算)")
print(f"x | y = {x | y} (位元 OR 運算)")
print(f"x ^ y = {x ^ y} (位元 XOR 運算)")

print("\n=== 運算子優先順序 ===")
print("Python運算子優先順序 (由高到低):")
print("1. () - 括號")
print("2. ** - 指數")
print("3. +, - - 正負號")
print("4. *, /, //, % - 乘除、整數除法取餘、取餘數")
print("5. +, - - 加減")
print("6. <<, >> - 位移")
print("7. &, |, ^ - 位元 AND、OR、XOR 運算")
print("8. >, <, >=, <=, ==, != - 比較運算")
print("9. not, and, or - 邏輯運算")

print("\n運算子優先順序範例:")
print(f"8 - 2 * 3 = {8 - 2 * 3}")
print(f"(1 + 2) * 3 - 4 = {(1 + 2) * 3 - 4}")
print(f"(1 + 2) ** 2 - 5 = {(1 + 2) ** 2 - 5}")
print(f"1 + 2 ** 3 // 2 = {1 + 2 ** 3 // 2}")
print(f"5 > 5 % 2 = {5 > 5 % 2}")
print(f"2 > 1 and 3 < 4 = {2 > 1 and 3 < 4}")