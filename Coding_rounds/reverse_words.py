"""Write a Python function that takes a sentence as input and returns the sentence with
the words reversed but in the original order. Example: Input: "Python is awesome"
Output: "nohtyP si emosewa" """

def reverse_words(sentence):

    sentence_lst = sentence.split()
    rev_lst=[]
    for word in sentence_lst:
        rev_lst.append(word[::-1])
    return ' '.join(rev_lst)
sentence = input("Enter the sentence: ")
print(reverse_words(sentence))