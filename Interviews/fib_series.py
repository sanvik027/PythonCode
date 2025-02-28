def fib_series(n):
    count =0
    a,b = 0,1
    while count <n:
        yield a # generator
        a,b =b,a+b
        count+=1

fib_gen = fib_series(10)
for i in fib_gen:
    print(i,end=' ')
