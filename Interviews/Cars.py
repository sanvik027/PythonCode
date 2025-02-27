class Cars:
    # constructor:
    def __init__(self,make,model,year):
        # instance variable:
        self.make = make
        self.model = model
        self.year = year

    def engine_start(self):
        return "Car started the Engine."

    def engine_stop(self):
        return "Car stopped the Engine."
    def braking(self):
        return "Brakes applied on the car."

class BMW(Cars):
    # constructor:
    def __init__(self,make,model,year,variant):
        super().__init__(make,model,year) # calling the parent class constructor
        self.variant = variant

    def sunroof(self):
        return "BMW Sunroof facility"

# Creating Object
bmw = BMW('BMW','Z8',2018,'petrol')
print(bmw.engine_start()) # accessing parent method
print(bmw.sunroof()) # accessing child method