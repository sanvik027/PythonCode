def unique_lst(lst):
    seen = set()
    unique_list=[x for x in lst if not(x in seen or seen.add(x))]
    return unique_list
print(unique_lst([1,2,3,8,4,5,1,2,3,8,9]))
