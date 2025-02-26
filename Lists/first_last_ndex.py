"""
Write a  function to find the first and last index of the given element of the list.
"""

def first_last_index(lst,num):
    index =[]
    for i in range(len(lst)):
        if num ==lst[i]:
            index.append(i)
    if index:
        result =(index[0],index[-1])
    else:
        result =(-1,-1)
    return result

lst = [1, 2, 3, 2, 4, 2]
num = 2
print(first_last_index(lst,num))