import random

# 14-1
def LinearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

A = [random.randint(1, 100) for i in range(50)]
print(A)
key = eval(input("Please input your key(1~100): "))

index = LinearSearch(A, key)
if index == -1:
    print("The key not found")
else:
    print("The key is valid, found key at index ", index)

# 14-2
def BinarySearch(arr, low, high, key):
    mid = low + (high - low)//2
    if low > high:
        return -1
    if arr[mid] == key:
        return mid
    elif arr[mid] > key:
        return BinarySearch(arr, low, mid - 1, key)
    else:
        return BinarySearch(arr, mid + 1, high, key)

A = [random.randint(1, 100) for i in range(50)]
A.sort()
print(A)
key = eval(input("Please input your key(1~100): "))

index = BinarySearch(A, 0, len(A) - 1 , key)
if index == -1:
    print("The key not found")
else:
    print("The key is valid, found key at index ", index)

# 14-3
def Bubble_Sort(A):
    for i in range(len(A)):
        for j in range(len(A) - i - 1):
            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp

A = [random.randint(1, 100) for i in range(5)]
print("Before sort: ", end = "")
print(A)
print("After sort: ", end = "")
Bubble_Sort(A)
print(A)

# 14-4
B = [i for i in range(1, 101)]
random.shuffle(B)
print("Before sort: ", end = "")
print(B)
print("After sort: ", end = "")
Bubble_Sort(B)
print(B)

# 14-5
def Insertion_Sort(A):
    for i in range(1, len(A)):
       j = i - 1
       key = A[i]
       while j >= 0 and key < A[j]:
           A[j + 1] = A[j]
           j -= 1
       A[j + 1] = key

A = [random.randint(1, 100) for i in range(5)]
print("Before sort: ", end = "")
print(A)
print("After sort: ", end = "")
Insertion_Sort(A)
print(A)

# 14-6
B = [i for i in range(1, 101)]
random.shuffle(B)
print("Before sort: ", end = "")
print(B)
print("After sort: ", end = "")
Insertion_Sort(B)
print(B)