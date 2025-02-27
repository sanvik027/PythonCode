"""
Python Inheritance allows a class (child class) to acquire properties and methods of
another class (parent class). It supports hierarchical classification and promotes
 code reuse.
Types of Inheritance:
Single Inheritance: A child class inherits from a single parent class.
Multiple Inheritance: A child class inherits from more than one parent class.
Multilevel Inheritance: A child class inherits from a parent class, which in turn
inherits from another class.
Hierarchical Inheritance: Multiple child classes inherit from a single parent class.
Hybrid Inheritance: A combination of two or more types of inheritance.
"""
# single inheritance
class Dog: # parent class
    # constructor
    def __init__(self,name):
        # instance variable
        self.name = name
    def display_name(self):
        print(f"Dog's name : {self.name}")
class Labrador(Dog): # child class
    def sound(self):
        print("Labrador woofs")
# multilevel inheritance
class GuideDog(Labrador):
    def guides(self):
        print(f"{self.name} guides the way!")

# multiple inheritance
class Friendly:
    def greet(self):
        print("Friendly!")

class GoldenRetriever(Friendly,Dog):
    def sound(self):
        print("Golden retriever barks")

# Example usage
lab = Labrador("Buddy")
lab.display_name()
lab.sound()

guide_dog = GuideDog("Max")
guide_dog.display_name()
guide_dog.guides()

retriever = GoldenRetriever("Charlie")
retriever.display_name()
retriever.greet()
retriever.sound()