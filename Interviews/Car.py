class Car:
    # Constructor
    def __init__(self,make,model):
        # instance variable
        self.make = make
        self.model = model

    def display_info(self):
        return f"make : {self.make}, model: {self.model}"


# Creating an Object of the car class
car = Car("Tata","Punch")# constructor calles
print(car.display_info())
