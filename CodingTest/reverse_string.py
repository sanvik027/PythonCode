"""
Question 4: Write a Python script to reverse a string without using any
built-in functions like reversed() or [::-1] slicing. You should achieve this using a
loop.
"""
def reverse_str(s):
    rev_string = ""
    for  i in s:
        rev_string =i + rev_string
    return rev_string
print(reverse_str("HelloWorld"))