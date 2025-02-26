def sum_of_smallest(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

print(sum_of_smallest([12,45,32,5,2,25]))