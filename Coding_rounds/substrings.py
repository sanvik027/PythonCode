def find_all_substring(s):
    sub_string=[]
    for i in range(len(s)):
        for j in range(i,len(s)+1):
            substring = s[i:j]
            if ' 'not in substring:
                sub_string.append(substring)
    return sub_string

str = input("Enter the string : ")
result = find_all_substring(str)
print(result)
def find_all_substrings(s):
    return [s[i:j] for i in range(len(s)) for j in range(i + 1, len(s) + 1) if " " not in s[i:j]]
