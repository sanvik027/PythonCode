"""
write a function to add second and second last element in a list
"""


def add_items(numbers):
    """

    :param numbers:
    :return:
    """
    total = 0
    for i in range(0, len(numbers)):
        total = numbers[1] + numbers[len(numbers) - 2]
    return total
numbers= [1,2,3,4,5]
print(add_items(numbers))