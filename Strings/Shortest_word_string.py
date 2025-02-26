

def shortest_word(sentence):
    """

    :param sentence: takes a string as an input
    :return: returns the shortest word
    """
    words =sentence.split()
    shortest_word =min(words,key=len)
    return shortest_word
print(shortest_word("This is a sentence"))