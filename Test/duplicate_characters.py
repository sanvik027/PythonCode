
def find_duplicates(s):
    # convert to lower case
    s = s.lower()
    # dict to count occurance
    char_count ={}

    for ch in s:
        if ch in char_count:
            char_count[ch]+=1
        else:
            char_count[ch]=1
    # find duplicates
    duplicates = [ch for ch, count in char_count.items() if count>1]
    # unique = [ch for ch, count in char_count.items() if count ==1]
    return duplicates
print(find_duplicates("Tripti"))