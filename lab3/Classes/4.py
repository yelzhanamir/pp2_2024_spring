import math

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def show(self):
        return f"({self.x}, {self.y})"

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

# Example 
point1 = Point(3, 4)
point2 = Point(6, 8)
print("Coordinates of point1:", point1.show())  
point1.move(1, 2)
print("New coordinates of point1:", point1.show()) 
distance = point1.dist(point2)
print("Distance between point1 and point2:", distance)  