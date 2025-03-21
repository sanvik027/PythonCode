def is_palindrome(s):
    # convert to lower
    s = s.lower()
    rev_str = ""
    for ch in s:
        rev_str = ch+ rev_str

    if rev_str ==s:
        return True
    else:
        return False

print(is_palindrome("Madam"))