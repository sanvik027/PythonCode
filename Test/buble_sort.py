def buble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(0,n-i-1):
            if lst[j]> lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]

    return lst
# Test the function
numbers = [5, 2, 9, 1, 5, 6]
sorted_numbers = buble_sort(numbers)
print("Sorted List:", sorted_numbers)