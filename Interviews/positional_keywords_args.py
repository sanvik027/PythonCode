"""
*args and *kwargs are used to handle variable numbers of arguments in python.
*args is used to pass variable number of positional arguments,it collects
the extra arguments as a tuple.
 *kwargs are used to handle variable numbers of keywords arguments, it collects the
 extra arguments as a dictionary in key, value pairs"""



def add_nums(*args):
    total = 0
    for a in args:
        total+=a
    return total

result = add_nums(*(1,2,3,4))
print(result)

def show_info(**kwargs):
    dict_info= {}
    for key,value in kwargs.items():
        dict_info[key] =value
    return dict_info
print(show_info(**{'name': 'Ram', 'age': 33, 'city': 'Hanoi'}))
