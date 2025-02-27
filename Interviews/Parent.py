class Parent:
    @staticmethod
    def greet(msg):
        return f"Hello {msg}"

class Child(Parent):
    @staticmethod
    def greet(msg):
        return f"Hello {msg}"

# calling the parent method
msg= Parent.greet("Namaste")
print(msg)
# calling the overridden child method
msg1= Child.greet("Namaskar")
print(msg1)
# Creating an instance of the Child class and calling the static method
child_instance = Child()
print(child_instance.greet("Sasriakal"))