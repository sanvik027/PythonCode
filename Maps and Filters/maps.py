"""
map is a special function in python which takes any function and an iterable as input
parameter and returns a map object which is an iterator
"""
lst =['1','2''3','4','5']
res = map(int,lst) # map function takes int and a list and returns a map object
print(list(res)) # convert the map object to list and returns an integer list

# double each element of the given list
num =[1,2,3,4]

def double_num(num_lst):
    return num_lst*2

res = list(map(double_num,num))
print(res)

# double each element using lambda function
res1 = list(map(lambda x:x*2,num))
print(res1)

"""
Using map() with multiple iterables
We can use map() with multiple iterables if the function we are applying takes 
more than one argument.

Example: In this example, map() takes two iterables (num1 and num2)
and applies the lambda function to add corresponding elements from both lists.

"""
num1 = [1,2,3,4]
num2 = [5,6,7,8]

add_lst = list(map(lambda x,y : x +y,num1,num2))
print(add_lst)

# converting to upper case using map
s =['apple','banana','orange','cherry']
s_upper = map(str.upper,s)
print(list(s_upper))

# Extracting first character from string
first_lst = map(lambda x:x[0],s)
print(list(first_lst))

# Converting celsius to fahrenheit
celsius = [0, 20, 37, 100]
fahrenheit = map(lambda c: (c * 9/5) + 32, celsius)
print(list(fahrenheit))