"""
Question 3: Write a Python script to find the intersection of two lists.
The intersection of two lists is a list containing all the elements that are common to both lists,
without any duplicates.
"""
def intersection_list(lst1,lst2):
    seen1 = set(lst1)
    seen2 = set(lst2)
    return list(seen1.intersection(seen2))

lst1 = [1,2,3,4,1,2,3]
lst2 = [2,3,4,1,5,6,2]
print(intersection_list(lst1,lst2))
