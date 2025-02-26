def find_occurrence_of_character(word,character):
    """

    :param word: takes the word as input
    :param character: takes the character for which the count will occur
    :return: the count of the character
    """
    if not isinstance(word,str):
        raise TypeError("Enter only String")
    #Set the counter to zero
    count =0
    # for loop to iterate through the string
    for w in word:
        # check and increment the count if the condition is true
        if w in character:
            count+=1
    # returns the count
    return count

word = input("Enter any word : ")
character = input("Enter any character to search: ")
print(find_occurrence_of_character(word,character))