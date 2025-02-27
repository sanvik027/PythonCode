class Shapes:
    # constructor:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def cal_area(self): #parent method
        pass

class Rectangle(Shapes):
    def cal_area(self):# overridden method
        return self.length * self.breadth

class Square(Shapes):
    def cal_area(self): # overridden method
        return self.length ** 2

# creating objects
rect = Rectangle(2,5)
ar_rect = rect.cal_area()
print(f"Area---> Rectangle: {ar_rect}")

sqr = Square(2,6)
ar_sqr = sqr.cal_area()
print(f"Area---> Square: {ar_sqr}")