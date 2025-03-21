def check_armstrong(n):
    total =0
    num_digits = len(str(n))
    n1 = n

    while n !=0:
        num = n %10
        total = num ** num_digits + total
        n = n//10
    if total ==n1:
        return True
    else:
        return False

number = int(input("Enter the number : "))
armstrong = check_armstrong(number)
print(f"The given number {number} is armstrong: {armstrong}")