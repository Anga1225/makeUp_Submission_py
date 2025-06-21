# Console 執行之程式碼
# =================
# 列表 (List) 練習
# =================
print("\n=== 列表 (List) 練習 ===")

# 建立列表
print("\n1. 建立和操作列表:")
list1 = []
list2 = [1, 2, 3, 4, 5]
list3 = [1, 2, 3, 3.5, 4.4, 5.1]
list4 = ["Mary", "Tim", "Nancy"]
list5 = ["Blue", "Red"]

print(f"空列表: {list1}")
print(f"整數列表: {list2}")
print(f"混合數字列表: {list3}")
print(f"字串列表: {list4}")
print(f"顏色列表: {list5}")

# 列表索引和切片
print("\n2. 列表索引和切片:")
print(f"list2[1]: {list2[1]}")
print(f"list2[1:3]: {list2[1:3]}")
print(f"list2[-1]: {list2[-1]}")
print(f"list2[:3]: {list2[:3]}")

print("\n3. 列表方法:")
list6 = [1, 2, 3, 4, 5]
print(f"原始列表: {list6}")

list6.append(6)
print(f"append(6)後: {list6}")

list6.insert(0, 0)
print(f"insert(0, 0)後: {list6}")

list6.remove(3)
print(f"remove(3)後: {list6}")

popped = list6.pop()
print(f"pop()彈出的元素: {popped}")
print(f"pop()後的列表: {list6}")

list7 = [1, 2, 3, 4, 5]
print(f"\nlist7: {list7}")
print(f"count(3): {list7.count(3)}")

print(f"index(4): {list7.index(4)}")

list8 = [5, 2, 8, 1, 9]
print(f"\n排序前: {list8}")
list8.sort()
print(f"sort()後: {list8}")

list8.reverse()
print(f"reverse()後: {list8}")

print("\n4. 列表推導式:")
squares = [i ** 2 for i in range(5)]
print(f"平方數列表: {squares}")

even_numbers = [i for i in range(10) if i % 2 == 0]
print(f"偶數列表: {even_numbers}")

# =================
# 元組 (Tuple) 練習
# =================
print("\n=== 元組 (Tuple) 練習 ===")

print("\n1. 建立和操作元組:")
tuple1 = ()
tuple2 = (1, 2, 3, 4, 5)
tuple3 = ("go", "me", "we")
tuple4 = (2,)

print(f"空元組: {tuple1}")
print(f"數字元組: {tuple2}")
print(f"字串元組: {tuple3}")
print(f"單元素元組: {tuple4}")

print(f"\ntuple2[0]: {tuple2[0]}")
print(f"tuple2[1:3]: {tuple2[1:3]}")

print("\n2. 元組方法:")
print(f"tuple2.count(3): {tuple2.count(3)}")
print(f"tuple2.index(4): {tuple2.index(4)}")

print("\n3. 元組解包:")
point = (3, 4)
x, y = point
print(f"座標點: {point}")
print(f"x = {x}, y = {y}")

print("\n4. 元組與列表轉換:")
list_from_tuple = list(tuple2)
tuple_from_list = tuple(list2)
print(f"元組轉列表: {list_from_tuple}")
print(f"列表轉元組: {tuple_from_list}")

# =================
# 集合 (Set) 練習
# =================
print("\n=== 集合 (Set) 練習 ===")

print("\n1. 建立和操作集合:")
set1 = set()
set2 = {1, 2, 3, 4, 5}
set3 = {"go", "me", "we"}

print(f"空集合: {set1}")
print(f"數字集合: {set2}")
print(f"字串集合: {set3}")

print("\n2. 集合操作:")
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(f"集合A: {set_a}")
print(f"集合B: {set_b}")

# 聯集 (Union)
union_set = set_a | set_b  # 或 set_a.union(set_b)
print(f"聯集 A|B: {union_set}")

# 交集 (Intersection)
intersection_set = set_a & set_b  # 或 set_a.intersection(set_b)
print(f"交集 A&B: {intersection_set}")

# 差集 (Difference)
difference_set = set_a - set_b  # 或 set_a.difference(set_b)
print(f"差集 A-B: {difference_set}")

# 對稱差集 (Symmetric Difference)
sym_diff_set = set_a ^ set_b  # 或 set_a.symmetric_difference(set_b)
print(f"對稱差集 A^B: {sym_diff_set}")

print("\n3. 集合方法:")
test_set = {1, 2, 3}
print(f"原始集合: {test_set}")

test_set.add(4)
print(f"add(4)後: {test_set}")

test_set.remove(2)
print(f"remove(2)後: {test_set}")

test_set.discard(5)
print(f"discard(5)後: {test_set}")

print("\n4. 集合推導式:")
squares_set = {i ** 2 for i in range(5)}
print(f"平方數集合: {squares_set}")

# =================
# 字典 (Dictionary) 練習
# =================
print("\n=== 字典 (Dictionary) 練習 ===")

print("\n1. 建立和操作字典:")
dict1 = {}
dict2 = {"name": "John", "age": 30, "city": "New York"}
dict3 = {1: "one", 2: "two", 3: "three"}

print(f"空字典: {dict1}")
print(f"資訊字典: {dict2}")
print(f"數字字典: {dict3}")

print(f"\n取得值 dict2['name']: {dict2['name']}")
print(f"取得值 dict2.get('age'): {dict2.get('age')}")
print(f"取得值 dict2.get('country', 'Unknown'): {dict2.get('country', 'Unknown')}")

print(f"\n字典鍵: {dict2.keys()}")
print(f"字典值: {dict2.values()}")
print(f"字典項目: {dict2.items()}")
# 字典推導式
print("\n2. 字典推導式:")
squares_dict = {i: i ** 2 for i in range(5)}
print(f"平方數字典: {squares_dict}")

# 12-1
print("stack")
n = 0
stack = []
while True:
    print("------------------")
    print("stack operation")
    print("option 1: Push")
    print("option 2: Pop")
    print("option 3: Display")
    print("option 4: Quit")
    print("------------------")

    choice = eval(input("Input your choice: "))
    if choice == 1:
        key = eval(input("Input your key: "))
        stack.append(key)
        n += 1
    elif choice == 2:
        if n > 0:
            key = stack.pop()
            print("Pop key: ", key)
            n -= 1
        else:
            print("Stack is empty")
    elif choice == 3:
        print("Stack: ", stack)
    else:
        break

# 12-2
print("Queue")
n = 0
queue = []
while True:
    print("------------------")
    print("Queue operation")
    print("option 1: Enqueue")
    print("option 2: dequeue")
    print("option 3: Display")
    print("option 4: Quit")
    print("------------------")

    choice = eval(input("Input your choice: "))
    if choice == 1:
        key = eval(input("Input your key: "))
        queue.append(key)
        n += 1
    elif choice == 2:
        if n > 0:
            key = queue.pop(0)
            print("Pop key: ", key)
            n -= 1
        else:
            print("Queue is empty")
    elif choice == 3:
        print("Queue: ", queue)
    else:
        break

# 12-3
a = [1, 2, 3, 4]
b = [2, 4, 3, 1]

c = [0 for i in range(4)]
for i in range(4):
    c[i] = a[i] + b[i]
print("向量加法")
print(c)

scalar = 3
for i in range(4):
    c[i] = scalar * a[i]
print("向量乘法")
print(c)

# 12-4
def Matrix_Add(A, B):
    n = len(A)
    c = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            c[i][j] = A[i][j] + B[i][j]
    return c
def Matrix_Multiply(A, B):
    n = len(A)
    c = [[0 for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                c[i][j] = c[i][j] + A[i][k] * B[k][j]

    return c

A = [[1, 2], [3, 4]]
B = [[2, 4], [3, 1]]

c = Matrix_Add(A, B)
print("矩陣乘法")
print(c)

c = Matrix_Multiply(A, B)
print("矩陣乘法")
print(c)