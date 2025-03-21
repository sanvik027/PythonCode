"""
Question 1: Write a Python script to find the second largest element in a list.
You should handle cases where the
list might have duplicate elements or might not have at least two unique elements.
"""

def second_largest(lst):
    seen= set()
    for i in lst:
        if i not in seen:
            seen.add(i)

    return list(seen)
result = sorted(second_largest([1,1,2,3,4,5,5,6,1,2,3,7,4]),reverse=True)
print(result[1])
