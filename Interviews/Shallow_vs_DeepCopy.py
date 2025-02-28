"""
A shallow copy creates a new object but does create copies of the nested objects , if
we change anything on the nested object then it will impact the original object

A deep copy copies the original objects and also recursively creates copies of nested
objects hence changing the nested object doesn't effect the original object """

# shallow copy eg
import copy
original_list = [1,[2,3],4,5]
shallow_copied_list =copy.copy(original_list)
# changing the value of copied list
shallow_copied_list[1][0]='Changed list'
print(original_list)
print(shallow_copied_list)

# deep copy eg
org_lst = [1,2,3,'a','b',5]
deep_copied_lst = copy.deepcopy(org_lst)
# changing the value of the copied list
deep_copied_lst[3]=4
print(org_lst)
print(deep_copied_lst)