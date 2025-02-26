"""Write a function to replace an item in a list with a new value
if the item is found in the list"""
def replace_item(lst, old_item, new_item):
    """

    :param lst:
    :param old_item:
    :param new_item:
    :return:
    """
    for i in range(0,len(lst)):
        if lst[i] == old_item:
            lst[i]= new_item
    return lst
lst =['apple','banana','cherry']
old_item = 'banana'
new_item ='orange'
print(replace_item(lst,old_item,new_item))