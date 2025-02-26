def is_prime(num):
    if num <2:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i ==0:
            return False
    return True

def prime_numbers(limit):
    num =2
    while num <=limit:
        if is_prime(num):
            yield num
        num+=1

for prime in prime_numbers(20):
    print(prime)