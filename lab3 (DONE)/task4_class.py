import math

class Point:
    def __init__(self):
        self.x = float(input("Your x coordinate: "))  
        self.y = float(input("Your y coordinate: "))  

    def show(self):
        print(({self.x}, {self.y})) 

    def move(self):
        self.x = float(input("Enter one more x coordinate: "))  
        self.y = float(input("Enter one more y coordinate: "))  

    def dist(self, other_point):
        distance = math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)
        return distance  

point1 = Point()
point1.show()

point2 = Point()
point2.show()

print({point1.dist(point2)})
