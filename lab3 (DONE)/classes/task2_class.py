class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self):
        self.length=float(input("Length: "))

    def area(self):
        return self.length ** 2

square = Square()
print(square.area())  
