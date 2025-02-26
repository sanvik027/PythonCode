def filter_list(lst):
    seen = set()
    filtered_list=[]
    for x in lst:
        if x not in seen:
            seen.add(x)
            filtered_list.append(x)
    return filtered_list
print(filter_list([1,2,3,4,2,3,6,7,1]))