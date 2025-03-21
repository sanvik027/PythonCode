fruits =['apple','orange','cherry']
# using enumarate to get index and value
for index, fruit in enumerate(fruits):
    print(f"index:{index}, fruits:{fruit}")

def fib_creator(n):
    count = 0
    a,b =0,1
    while count < n:
        yield a
        a,b = b,b+a
        count+=1

fib_gen = fib_creator(10)

for num in fib_gen:
    print(num, end=' ')

