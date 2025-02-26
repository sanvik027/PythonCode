import re
def filter_string(s):
    filtered_str = re.sub(r'[^a-zA-z]','',s)
    return filtered_str
s = input("Enter an alphanumeric string: ")
print(filter_string(s))

def fltr_string(a):
    filter_st = ""
    for i in a:
        if i.isalpha():
            filter_st+=i
    return filter_st
print(fltr_string("TR@@@!Q112Deods"))