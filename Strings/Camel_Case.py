def convert_to_camel_case(s):
    """

    :param s:
    :return:
    """

    # If the phrase is empty, return an empty string
    if not s:
        return ""
    word = s.lower()
    split_word = word.split()
    result = split_word[0]
    for w in split_word[1:]:
        result = result+ w.title()
    return result
print(convert_to_camel_case("hello"))