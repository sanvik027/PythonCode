"""
Write a function to eliminate all odd numbers from a list
"""
def eliminate_odd_numbers(numbers):
    return [num for num in numbers if num%2==0]
numbers =[1,2,3,4,5]
print(eliminate_odd_numbers(numbers))