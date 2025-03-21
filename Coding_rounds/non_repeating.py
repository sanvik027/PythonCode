def get_non_repeating_char(s):
    s = s.lower()
    char_count={}
    for ch in s:
        if ch in char_count:
            char_count[ch]+=1
        else:
            char_count[ch]=1

    unique_lst =[ch for ch,count in char_count.items() if count ==1]
    if len(unique_lst)<1:
        return "String doesn't contain unique characters "
    else:
        return unique_lst[0]
inp_str = input("Enter the string: ")
print(get_non_repeating_char(inp_str))

