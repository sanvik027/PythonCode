"""
Write a Python function that:

Takes a list of integers as input.

Finds and returns the second largest number in the list.

Handles cases where the list has duplicate values or fewer than two unique numbers
gracefully (e.g., raises an exception or returns an appropriate message).
"""
def find_second_largest(lst):
    def get_unique_list(dup_lst):
        seen =set()
        unique_lst =[x for x in dup_lst if not(x in seen)or(seen.add(x))]
        return unique_lst
    unique_lst = get_unique_list(lst)
    if len(unique_lst)<2:
        return f"Error: List must have two unique element"

    unique_lst.sort(reverse=True)
    return unique_lst[1]

# Example usage
numbers = [4, 2, 8, 8, 1, 9, 4]
result = find_second_largest(numbers)
print(f"The second largest number is: {result}")



