""""
The property() function in Python is used to create managed attributes, meaning you can
 control access to an attribute of a class while keeping the syntax clean and easy to
  use. It allows you to define getter, setter, and deleter methods for an attribute
  by exposing it as a property. This is especially useful when you want to add logic
  (like validation or computation) to an attribute without
  exposing those methods explicitly.

    Why is property() Useful?
    Encapsulation: It allows you to hide implementation details and control
    how an attribute is accessed or modified.

    Code Readability: Provides a clean and intuitive way to interact with object
    attributes without explicitly calling methods.
"""
class Circle:
    def __init__(self,radius):
        self._radius = radius

    # getter for radius
    def get_radius(self):
        return self._radius
    # setter for radius
    def set_radius(self,value):
        if value<=0:
            raise ValueError("Radius should be postive")
        self._radius = value

    # deleter for radius
    def del_radius(self):
        print("Deleting Radius")
        del self._radius

    # using proprty to manage radius
    radius = property(get_radius,set_radius,del_radius)


# Usage
c = Circle(5)
print(c.radius)  # Output: 5 (getter is called)

c.radius = 10     # Calls setter to update the radius
print(c.radius)   # Output: 10

del c.radius      # Calls the deleter

