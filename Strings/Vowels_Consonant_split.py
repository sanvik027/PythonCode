def split_string(s):
    """

    :param s:
    :return:
    """
    vowels = str()
    consonant = str()

    for i in s:
        w = i.lower()
        if w in ['a','e','i','o','u']:
            vowels+=i
        else:
            consonant+=i
    result = (vowels,consonant)
    return result
print(split_string("Hello"))