def __init__(self, width, height):
self.width = width
self.height = height
def calculate_area(self):
return self.width * self.height
rectangle = Rectangle(3, 4)
print(f"Area of the rectangle: {rectangle.calculate_area()}")

import math

class Circle:
def __init__(self, radius):
self.radius = radius
def calculate_area(self):
return math.pi * self.radius ** 2
def calculate_circumference(self):
return 2 * math.pi * self.radius
circle = Circle(5)
print(f"Area of the circle: {circle.calculate_area()}")

print(f"Circumference of the circle:
{circle.calculate_circumference()}")
