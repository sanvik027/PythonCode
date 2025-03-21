def check_palindrome(s):
    s=s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1  # Move left pointer forward
        right -= 1  # Move right pointer backward
    return True  # If all characters match, it's a palindrome

# Example usage
string = input("Enter a string: ")
print(f"The string '{string}' is a palindrome: {check_palindrome(string)}")
