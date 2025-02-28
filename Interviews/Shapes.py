from abc import ABC, abstractmethod
class Shape:
    @abstractmethod
    def cal_area(self):
        pass
    @abstractmethod
    def cal_perimeter(self):
        pass

class Rectangle(Shape):
    # constructor
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def cal_area(self):
        return round(self.length * self.breadth)
    def cal_perimeter(self):
        return round(2 *(self.length * self.breadth))

rect = Rectangle(2.5,5.6)
ar_rect = rect.cal_area()
pr_rect = rect.cal_perimeter()
print(f"Area----> {ar_rect}")
print(f"Perimeter---> {pr_rect}")