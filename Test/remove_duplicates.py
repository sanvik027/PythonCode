def remove_duplicate_words(s):
    # convert to lower:
    s = s.lower()
    words = s.split()
    words_count= {}
    for ch in words:
        if ch in words_count:
            words_count[ch]+=1
        else:
            words_count[ch]=1

    unique = [ch for ch,count in words_count.items() if count==1]
    return unique


word = input("Enter any word: ")
print(remove_duplicate_words(word))