def count_occurrence_word(text):

    if not isinstance(text,str):
        print("Unsupported argument type")
        raise TypeError("Input should be a string")
    if not text:
        return {}
    letter_count = {}
    for word in text:
        if word in letter_count:
            letter_count[word]+=1
        else:
            letter_count[word]=1
    return letter_count

text = "hello"
print(count_occurrence_word(text))



