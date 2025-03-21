def remove_duplicates_list(lst):
    seen=set()
    unique_list = [x for x in lst if not(( x in seen) or seen.add(x))]
    return unique_list

print(remove_duplicates_list([1,2,5,1,3,5,7,8,2,7,7,7]))