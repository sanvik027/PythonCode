class Animal:
    # constructor
    def __init__(self,name,age):
        self.age = age
        self.name = name

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def __init__(self,name,age,species):
        # calling the parent constructor using super keyword
        super().__init__(name,age)
        self.species = species
    def sound(self):
        print("Dog Woofs !!!") # overridden method

# object creation
dog = Dog("James",2,"Labrador")
print(dog.name, dog.age,dog.species)
dog.sound()
