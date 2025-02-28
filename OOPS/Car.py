class Car:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.make},{self.model},{self.year}"
    def start_engine(self):
        return "Car engine started."



# creating object for the car class
car = Car("Tata","Punch",2021)
print(car.display_info())