def add_ends(number, i=0):
    # check if the list is empty.
    if not numbers:
        print("List is empty")
        return None

    # check if the index is valid or not
    if index < 0 or index >= len(number):
        print("Index out of range : Please enter a valid index.")
        return None
    total = 0
    # add the given index
    total += number[i]
    # add a logic to check if the last element not be equal to the given index.
    if number[i] != number[len(number) - 1]:
        total += number[len(number) - 1]
    return total


index = input("Enter any index or press enter for 0: ")
numbers = [1, 2, 3, 4, 5]
# if index is other than zero
if index:
    index = int(index)
else:
    index = 0
print(add_ends(numbers, index))
