def to_from_list(n):
    if isinstance(n,list):
        result = int(''.join(map(str,n)))

    else:
        result = list(map(int,str(n)))
    return result


print(to_from_list([1,2,4,3]))