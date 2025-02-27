class Dog:
    # Class variable
    species = "Canine"

    # Constructor
    def __init__(self,name,age):
        # instance Variables
        self.name = name
        self.age = age

# Create Objects
dog1 = Dog("sheldon",12)
dog2 = Dog("tommy",5)

# Accessing class and instance variables
print(dog1.species) # class variable
print(dog1.name) # instance variable
print(dog1.age)  # instance variable
print(dog2.name)
print(dog2.age)
# modify instance variable
dog1.name ='aamir'
# modify class variable
Dog.species = 'Feline'
print("printing the values after updates:")
print(dog1.name)
print(dog2.name)
print(dog1.species)
print(dog2.species)
"""Explanation:
Class Variable (species): Shared by all instances of the class. 
Changing Dog.species affects all objects, as it’s a property of the class itself.
Instance Variables (name, age): Defined in the __init__ method. 
Unique to each instance (e.g., dog1.name and dog2.name are different).
Accessing Variables: Class variables can be accessed via the class name (Dog.species) 
or an object (dog1.species). Instance variables are accessed via the object (dog1.name).
Updating Variables: Changing Dog.species affects all instances. 
Changing dog1.name only affects dog1 and does not impact dog2.
"""