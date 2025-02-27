from collections import Counter

def count_occurrence(s):
    char_count = Counter(s.lower())
    return char_count
word = input("Enter the word: ")
print(count_occurrence(word))

def count_str(a):
    item_count=dict()
    for item in a:
        if item in item_count:
            item_count[item]+=1
        else:
            item_count[item]=1
    return item_count

print(count_str(word))