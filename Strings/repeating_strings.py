def first_repeating_char(s):
    """

    :param s:
    :return:
    """
    new_s = ""
    repeat_lst = []
    for i in s:
        if i not in new_s:
            new_s+=i
        else:
            repeat_lst.append(i)
    if len(repeat_lst)>0:
        return repeat_lst[0]
    else:
        return "No repeating characters"


def first_repeating_chars(s):
    seen = set ()
    for char in s:
        if char in seen:
            return char
        seen.add(char)
    return "No repeating characters"

strs = "racecar"
print(first_repeating_chars(strs))