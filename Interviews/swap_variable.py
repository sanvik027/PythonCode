def swap_variable(a,b): # 3,4
    a =a+b # 7
    b = a-b # 3
    a = a-b # 4
    return a,b

print(swap_variable(3,4))