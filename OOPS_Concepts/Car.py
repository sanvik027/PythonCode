class Car:
    # constructor
    def __init__(self,make,model):
        # instance variables
        self.make = make
        self.model = model

    def no_of_wheels(self,wheels):
        return wheels

    def passanger_limit(self,pass_limit):
        return pass_limit

class LuxuryCar:
    #constructor
    def __init__(self,segment,cost):
        # instance variable
        self.segment = segment
        self.cost = cost

    def feature(self,features):
        return  features

    def braking_system(self,braking):
        return braking

class Audi(Car,LuxuryCar):

    # constructor
    def __init__(self,year):
        super.__init__(self.make,self.model)
        super.__init__(self.segment,self.cost)
        self.year = year

    def disp_info(self):
        print(self.make)
        print(self.segment)
        print(self.model)
        print(self.cost)
        print(self.year)


# creating Object:
audi = Audi(2021)
audi.disp_info()
no_of_wheels = audi.no_of_wheels(4)
print(f"No of wheels: {no_of_wheels}")
features_lst =['Camera','Remote sensing','Power Window','Moonroof']
print(f"Features of Audi: {audi.feature(features_lst)}")
