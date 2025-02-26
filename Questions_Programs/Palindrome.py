def is_palindrome(s):
    cleaned_string = ''.join(s.lower() for char in s if char.isalnum())
    left = 0
    right =len(cleaned_string)-1

    while left < right:
        if cleaned_string[left]!=cleaned_string[right]:
            return False
        left+=1
        right-=1
    return True
s = input("Enter the word: ")
print(is_palindrome(s))

