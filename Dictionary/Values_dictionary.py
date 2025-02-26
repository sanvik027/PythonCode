def get_value_searched_dict(my_dict,value_searched):
    """

    :param my_dict: accepts a dictionary
           value_searched: the value user wants to search in the dictionary
    :return: True if the value is found else False if the value is not found.
    """
    # Checking the input type to be a dictionary else raise type error
    if not isinstance(my_dict,dict):
        raise TypeError("Please enter a dictionary")

    # set default flag to False
    flag = False

    # iterating through the dict using for loop:
    for key in my_dict:
        # check if the searched value is in the dictionary:
        if my_dict[key] == value_searched:
            # set flag to true:
            flag = True
    if flag:
        return "Value Found in the dictionary"
    else:
        return "Value not Found in the dictionary"


my_dict= {1:"Raymond", 2:"Vimal", 3:"Arvind"}
value_searched = input("Enter the value to be searched in the dictionary: ")
print(get_value_searched_dict(my_dict,value_searched))