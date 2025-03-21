import copy
# shallow copy
org_list = [1,[2,3],4,5]
shallow_copied_lst = copy.copy(org_list)
shallow_copied_lst[1][0] = 7
# original list changed
print(org_list)

# deep copy
fruits = ['apple','banana','pear']
deep_copied_fruits= copy.deepcopy(fruits)
deep_copied_fruits.append("grapes")
# changes to fruits
print(deep_copied_fruits)
# original list remained intact
print(fruits)