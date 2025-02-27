class Vehicle:
    def __init__(self,make,model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"

class Car(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model)
        self.year = year

    def car_info(self):
        return f"{self.make} {self.model} {self.year}"

my_car = Car("Honda","Civic",2018)
print(my_car.car_info())
