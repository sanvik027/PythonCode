# List example
my_list = [1, 2, 2, 3, 4]
print("List:", my_list)
print("Second element:", my_list[1])  # Accessing by index

# Set example
my_set = {1, 2, 2, 3, 4}
print("Set:", my_set)
# Uncommenting the line below will raise an error because sets do not support indexing
# print("Second element:", my_set[1])

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference:", set1 - set2)
print("Symmetric Difference:", set1 ^ set2)
