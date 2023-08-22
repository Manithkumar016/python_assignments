
# 9) Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle. 

class Circle:
    def __init__(self,radius) -> None:
        self.radius=radius
    def area(self):
        print(f"Area of the circle with radius {self.radius} is : {3.14*self.radius**2}")

    def perimeter(self):
        print(f"Perimeter of the circle with radius {self.radius} is : {2*3.14*self.radius}")

c = Circle(7)
c.area()
c.perimeter()