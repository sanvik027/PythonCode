def is_prime(n):
    count =0
    if n <2:
        return False
    else:
        for i in range(1,n+1):
            if n % i == 0:
                count+=1
    if count == 2:
        return True
    else:
        return False

print(is_prime(1))