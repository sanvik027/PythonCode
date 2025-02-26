def get_largest_number(numbers):
    numbers.sort()
    return numbers[-1]
def get_smallest_number(numbers):
    """

    :param numbers: numeric list only
    :return: the smallest number in the list
    """
    numbers.sort()
    return numbers[0]
def get_largest_number_list(numbers):
    largest =numbers[0]
    for number in numbers:
        if largest < number:
            largest =number
    return largest

def get_smallest_number_list(numbers):
    """

    :param numbers:
    :return:
    """
    smallest = numbers[0]
    for number in numbers:
        if smallest > number:
            smallest = number
    return smallest

numbers =[10,45,62,-1,54,32,21]
print(get_largest_number_list(numbers))
print(get_largest_number(numbers))
print(get_smallest_number_list(numbers))