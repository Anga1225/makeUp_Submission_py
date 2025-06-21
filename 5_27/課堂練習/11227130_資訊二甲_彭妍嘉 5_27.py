# 13-1
import math

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        return self.radius * self.radius * math.pi
    def getPerimeter(self):
        return self.radius * 2 * math.pi

circle1 = Circle(5)
print("First circle object")
print("First circle's area:", circle1.getArea())
print("First circle's perimeter:", circle1.getPerimeter())
circle2 = Circle(10)
print("Second circle object")
print("Second circle's area:", circle2.getArea())
print("Second circle's perimeter:", circle2.getPerimeter())
# 13-2
class Student:
    def __init__(self,name,height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def getName(self):
        return self.name
    def getHeight(self):
        return self.height
    def getWeight(self):
        return self.weight
    def getBMI(self):
        return self.weight/(self.height/100)**2
student1 = Student("張曉明", 170, 70)
print("Student name: ", student1.getName())
print("student height: ", student1.getHeight())
print("student weight: ", student1.getWeight())
print("student BMI: ", student1.getBMI())
student2 = Student("阿敏", 169, 66)
print("student name: ", student2.getName())
print("student height: ", student2.getHeight())
print("student weight: ", student2.getWeight())
print("student BMI: ", student2.getBMI())

#13-3
class Stack:
    def __init__(self):
        self.s = []
    def isEmpty(self):
        return self.s == []
    def Push(self, key):
        self.s.append(key)
    def Pop(self):
        if self.isEmpty():
            print("Stack is empty (Underflow)")
            return None
        else:
            return self.s.pop()
    def Display(self):
        print("Stack: ", end = "")
        print(self.s)
s = Stack()
s.Push(1)
s.Push(2)
s.Push(3)
s.Pop()
s.Display()

#13-4
class Queue:
    def __init__(self):
        self.Q = []
    def isEmpty(self):
        return self.Q == []
    def enQueue(self, item):
        self.Q.append(item)
    def deQueue(self):
        if self.isEmpty():
            print("Underflow")
            return None
        else:
            return self.Q.pop(0)
    def Display(self):
        print("Queue: ", end = "")
        print(self.Q)
Q = Queue()
Q.enQueue(1)
Q.enQueue(2)
Q.enQueue(3)
Q.deQueue()
Q.Display()

#13-5
class DisjointSet:
    def __init__(self, n):
        self.set = [i for i in range(n + 1)]
        self.n = n
    def Find(self, key):
        while self.set[key] != key:
            key = self.set[key]
        return key
    def Union(self, a, b):
        if self.Find(a) < self.Find(b):
            for i in range(self.n + 1):
                if self.Find(i) == self.Find(b):
                    self.set[i] = self.Find(a)
        else:
            for i in range(self.n + 1):
                if self.Find(i) == self.Find(a):
                    self.set[i] = self.Find(b)
    def Display(self):
        print("DisjointSet: ", end = "")
        for i in range(1, self.n + 1):
            if self.Find(i) == i:
                print("{ ", end = "")
                print(i, end = " ")
                for j in range(i + 1, self.n + 1):
                    if self.Find(j) == i:
                        print(",", end = "")
                        print(j, end = " ")
                print("},", end = "")
        print()

n = 8
S = DisjointSet(n)
S.Union(1, 2)
S.Union(1, 3)
S.Union(4, 5)
S.Union(6, 7)
S.Union(7, 8)
S.Display()
for i in range(1, n + 1):
    print("Find(%d) = %d" % (i, S.Find(i)))

