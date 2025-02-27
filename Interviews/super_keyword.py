class Vehicle:
    # constructor
    def __init__(self,make,model,year):
        # instance variable
        self.make = make
        self.model = model
        self.year = year



class Car(Vehicle):
    # constructor
    def __init__(self,make,model,year,variant):
        # calling the parent class constructor inside child class
        super().__init__(make,model,year)
        self.variant = variant

    def display_info(self):
        return (f"Make :{self.make}, Model : {self.model},"
                f" Year : {self.year}, Variant : {self.variant}")
# object creation
car = Car("Tata","Punch",2021,"i-CNG")
print(car.display_info())