def find_missing_letter(chars):
    complete_set = set(chr(c) for c in range(ord(chars[0]), ord(chars[-1]) + 1))
    given_set = set(chars)
    missing_letter = complete_set - given_set
    return missing_letter.pop() if missing_letter else None

chars = "abcefg"
missing_letter = find_missing_letter(chars)
print("The missing letter is:", missing_letter)
