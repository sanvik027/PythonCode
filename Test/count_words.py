def count_words(s):
    # split the strings into words
    words = s.split()
    # return the length of the word
    return len(words)

word = input("Enter the word : ")
word_length = count_words(word)
print(word_length)