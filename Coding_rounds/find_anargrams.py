"""
Question 10: Find Anagrams
Write a Python function that:

Takes two strings as input.

Checks if the two strings are anagrams of each other (i.e., the same letters in a
different order).

Returns True if they are anagrams, and False otherwise.

Example:

Input: "listen" and "silent"

Output: True

"""
def check_anagrams(s,s1):
    if len(s)!=len(s1):
        return f"The strings '{s}' and '{s1}' are not anagrams."
    sorted_s = sorted(s)
    sorted_s1 = sorted(s1)
    if sorted_s == sorted_s1:
        return True
    else:
        return False

str1 = input("Enter the first String: ")
str2 = input("Enter the second String: ")
result = check_anagrams(str1.lower(),str2.lower())
print(f"The given strings '{str1}' and '{str2}' are Anagrams: {result}")

