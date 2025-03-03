"""
Question 2: Write a Python script to check if a given string is a palindrome.
A palindrome is a string that reads the same forward and backward,
ignoring spaces, punctuation, and capitalization.
"""
import re
def check_palindrome(s):
    word = ''.join(re.sub('[^a-zA-Z]','',s).lower())
    rev_word = lambda word:''.join((word[i] for i in range(len(word)-1,-1,-1)))
    if rev_word(word) == word:
        return True
    else:
        return False

print(check_palindrome("R@acecar!!!"))