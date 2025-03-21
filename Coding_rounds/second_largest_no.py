def find_second_largest_no(lst):
    if len(lst)>1:
        for i in range(len(lst)):
            for j in range(0,len(lst)-1):
                if lst[j] < lst[j+1]:
                    lst[j],lst[j+1] = lst[j+1],lst[j]

        return lst[1]
    else:
        return "Error: Can't sort the list"

result = find_second_largest_no([1,5,2,4,89,43])
print(result)