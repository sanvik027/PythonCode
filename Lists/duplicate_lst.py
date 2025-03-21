def remove_duplicates(lst):
    seen = set()
    unique_lst = [x for x in lst if not((x in seen)or seen.add(x))]
    return unique_lst


num = [1, 2, 3, 2, 4, 5, 1, 6]
print(remove_duplicates(num))