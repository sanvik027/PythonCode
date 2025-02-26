def occurrence_character(s):
    char_count= dict()
    for ch in s:
        if ch in char_count:
            char_count[ch]+=1
        else:
            char_count[ch]=1
    return char_count
print(occurrence_character("Hello world !!!@"))

def extract_digit_from_string(a):
    digit_list= []
    for i in a:
        if i.isdigit():
            digit_list.append(i)
    return ''.join(digit_list)
word = input("Enter a alphanumeic string")
print(extract_digit_from_string(word))