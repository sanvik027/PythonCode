def fibonacci_gen(n):
    a,b = 0,1
    count = 0
    while count <n:
        yield a
        a,b =b,a+b
        count+=1

fib_gen = fibonacci_gen(10)
for num in fib_gen:
    print(num,end=' ')
