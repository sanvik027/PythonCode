import Strings


def divide_num(a,b):

    try:
        return a/b
    except Exception as e:
        print(f'Exception occurred : {e}')


print(divide_num(3,0))

def add_num(a, b):
    try:
        # Logic that may raise an exception
        if isinstance(a, str) or isinstance(b, str):
            raise TypeError("Strings are not allowed for addition.")
        result = a + b
    except TypeError as e:
        # Handle the exception
        return f"Error: {e}"
    else:
        # Executes if no exception occurs
        print("Addition successful!")
        return result
    finally:
        # Executes always
        print("Code executed successfully.")

# Test cases
print(add_num(4, 6))       # Output: Addition successful! Code executed successfully. 10
print(add_num("hello", 5)) # Output: Error: Strings are not allowed for addition. Code executed successfully.

import os
with open("../data/data.txt",'w')as file:
    file.write("New text")

