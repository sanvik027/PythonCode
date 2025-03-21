def fizz_buzz(limit):
    for i in range(1, limit + 1):
        # Check for multiples of both 3 and 5 first
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

# Call the function with a limit of 15
fizz_buzz(15)

