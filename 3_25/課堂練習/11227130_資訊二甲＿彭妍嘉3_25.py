import math

print("=== 基本數學函式 ===")
print(f"abs(-3.5) = {abs(-3.5)}")
print(f"int(2.5) = {int(2.5)}")
print(f"float(3) = {float(3)}")
print(f"max(2, 5) = {max(2, 5)}")
print(f"min(2, 5) = {min(2, 5)}")
print(f"pow(2, 5) = {pow(2, 5)}")
print(f"round(3.1416) = {round(3.1416)}")
print(f"round(3.1416, 2) = {round(3.1416, 2)}")

print("\n=== Math模組 ===")
print(f"math.pi = {math.pi}")
import math as m
print(f"m.pi = {m.pi}")
from math import *
print(f"pi = {pi}")

print(f"math.e = {math.e}")
print(f"math.log(math.e ** 2) = {math.log(math.e ** 2)}")
print(f"math.log2(1024) = {math.log2(1024)}")
print(f"math.log10(1000000) = {math.log10(1000000)}")
print(f"math.sqrt(2) = {math.sqrt(2)}")
print(f"math.sin(math.pi / 2) = {math.sin(math.pi / 2)}")
print(f"math.cos(math.pi / 2) = {math.cos(math.pi / 2)}")
print(f"math.tan(math.pi / 4) = {math.tan(math.pi / 4)}")
print(f"math.asin(1.0) = {math.asin(1.0)}")
print(f"math.acos(1.0) = {math.acos(1.0)}")
print(f"math.atan(1.0) * 4 = {math.atan(1.0) * 4}")
print(f"math.factorial(5) = {math.factorial(5)}")
print(f"math.degrees(math.pi) = {math.degrees(math.pi)}")
print(f"math.radians(30) = {math.radians(30)}")

print("\n=== 字元轉換函式 ===")
print(f"ord('A') = {ord('A')}")
print(f"ord('a') = {ord('a')}")
print(f"ord('你') = {ord('你')}")
print(f"ord('愛') = {ord('愛')}")
print(f"chr(65) = {chr(65)}")
print(f"chr(97) = {chr(97)}")
print(f"chr(20320) = {chr(20320)}")
print(f"chr(24859) = {chr(24859)}")

s1 = "A"
s2 = "Hello"
print(f"len('{s1}') = {len(s1)}")
print(f"len('{s2}') = {len(s2)}")

print("\n=== 字串運算 ===")
s1 = 'What'
s2 = 'time'
print(f"s1 + s2 = {s1 + s2}")
s1 = 'What'
print(f"s1 * 3 = {s1 * 3}")

print(f"'A' < 'a' = {'A' < 'a'}")
print(f"'A' < '你' = {'A' < '你'}")
print(f"'Yes' == 'No' = {'Yes' == 'No'}")
print(f"'Yes' != 'No' = {'Yes' != 'No'}")

print(f"'over' in 'Discover' = {'over' in 'Discover'}")
print(f"'order' in 'Discover' = {'order' in 'Discover'}")
print(f"'over' not in 'Discover' = {'over' not in 'Discover'}")
print(f"'order' not in 'Discover' = {'order' not in 'Discover'}")

print("\n=== 字串索引 ===")
s = "Welcome"
print(f"s[0] = {s[0]}")
print(f"s[1] = {s[1]}")
print(f"s[-1] = {s[-1]}")
print(f"s[-2] = {s[-2]}")
print(f"s[1:4] = {s[1:4]}")
print(f"s[:3] = {s[:3]}")
print(f"s[3:] = {s[3:]}")

print("\n=== 字串方法 ===")
s = "This is a book"
print(f"s.capitalize() = '{s.capitalize()}'")
print(f"s.lower() = '{s.lower()}'")
print(f"s.upper() = '{s.upper()}'")
print(f"s.swapcase() = '{s.swapcase()}'")
print(f"s.title() = '{s.title()}'")

s = "This is a book"
print(f"s.count('a') = {s.count('a')}")
print(f"s.count('is') = {s.count('is')}")
print(f"s.find('book') = {s.find('book')}")
print(f"s.index('book') = {s.index('book')}")
print(f"s.startswith('This') = {s.startswith('This')}")
print(f"s.endswith('apple') = {s.endswith('apple')}")

s1 = "123"
s2 = "ABC"
print(f"s1.isalnum() = {s1.isalnum()}")
print(f"s1.isalpha() = {s1.isalpha()}")
print(f"s2.isalnum() = {s2.isalnum()}")
print(f"s2.isalpha() = {s2.isalpha()}")

s1 = "abc"
s2 = "ABC"
print(f"s1.islower() = {s1.islower()}")
print(f"s1.isupper() = {s1.isupper()}")
print(f"s2.islower() = {s2.islower()}")
print(f"s2.isupper() = {s2.isupper()}")

s1 = "var123"
s2 = "123var"
s3 = "var:"
print(f"s1.isidentifier() = {s1.isidentifier()}")
print(f"s2.isidentifier() = {s2.isidentifier()}")
print(f"s3.isidentifier() = {s3.isidentifier()}")

s = "X X This is a book X X"
print(f"s.lstrip() = '{s.lstrip()}'")
print(f"s.rstrip() = '{s.rstrip()}'")
print(f"s.strip() = '{s.strip()}'")

s = "This is a book"
print(f"s.replace('book', 'pencil') = '{s.replace('book', 'pencil')}'")

s = "This is a book"
print(f"s.split() = {s.split()}")
s2 = "1,2,3,4"
print(f"s.split(',') = {s2.split(',')}")