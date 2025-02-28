class Car:
    # constructor
    def __init__(self,make,model,year):
        # instance variable.
        self.make = make
        self.model = model
        self.year = year

    def disp_info(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}"

# creating object
car = Car("Tata","Punch",2021) # consustructor is called and self takes the value of the car object
# displays the car information
print(car.disp_info())
