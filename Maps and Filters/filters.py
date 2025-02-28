"""
The filter method filters the given sequence with the help of a given function
that tests each element in the sequence to be true or not."""

def even(n):
    return n%2 == 0
a = [1,2,3,4,5,6,7]
b = filter(even,a)
print(list(b))

# Filter with lambda :
c =filter(lambda x: x % 2 !=0,a)
print(list(c))

# combining filter with map function
num_lst = [1,2,3,4,5,6,7,8,9,10]
even_lst = list(filter(lambda x : x %2 == 0,num_lst))
double_even_lst = list(map(lambda x : x*2,even_lst))
print(double_even_lst)