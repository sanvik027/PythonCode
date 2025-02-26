def even_num(limit):
    num = 0
    while num < limit:
        yield num
        num+=2

for even in even_num(10):
    print(even,end=" ")
