def common_lst(lst1,lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return list(set1.intersection(set2))
print(common_lst([1,2,3,4,5],[3,4,5,6,7]))