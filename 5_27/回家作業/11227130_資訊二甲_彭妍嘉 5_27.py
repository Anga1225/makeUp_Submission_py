class Rectangle:
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

w, h = eval(input("Please input the width and height of the rectangle: "))
r = Rectangle(w, h)
print("Rectangle area:", r.area())