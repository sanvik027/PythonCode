from abc import ABC , abstractmethod
class Shape(ABC):
    # abstract method
    @abstractmethod
    def area(self):
        pass
    # abstract method
    def perimeter(self):
        pass

class Rectangle(Shape):
    # constructor
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return round(self.length * self.breadth)

    def perimeter(self):
        return round(2 * self.length * self.breadth)


class Circle(Shape):
    # constructor
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return round(3.14 * self.radius ** 2)

    def perimeter(self):
        return round(2 * 3.14 * self.radius)

# creating objects
r_obj = Rectangle(2.59, 6.89)
rect_ar = r_obj.area()
rect_pr = r_obj.perimeter()
c_obj = Circle(3.45)
cir_ar = c_obj.area()
cir_pr = c_obj.perimeter()
# printing the values of rectangle
print(f"Area of the rectangle : {rect_ar}")
print(f"Perimeter of the rectangle: {rect_pr}")
# printing the values of circle
print(f"Area of the circle : {cir_ar}")
print(f"Perimeter of the circle: {cir_pr}")