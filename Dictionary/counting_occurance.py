def count_no_of_items(items):
    """"
    Args- "Takes a list as an input"
    returns a dictionary with key as main items and count as value.
     Raises:
        TypeError: If the input is not a list.
    """
    if not isinstance(items,list):
        raise TypeError("Input must be a list") # raise type error if the input type is not a list
    if not items:
        return {}  # Return an empty dictionary if the input list is empty
    item_count ={}
    # iterating through the list
    for item in items:
        # checks if the item is already present in the dictionary
        if item in item_count:
            # increment the counter to 1
            item_count[item]+= 1
        else:
            # Assign the counter to 1 if not present in the dictionary

            item_count[item]= 1
    # returns the final list
    return item_count
fruits = ["apple", "banana", "apple", "orange", "banana", "apple","mango"]
print(count_no_of_items(fruits))

#items = "apple"
#print(count_no_of_items(items))

city = []
print(count_no_of_items(city))