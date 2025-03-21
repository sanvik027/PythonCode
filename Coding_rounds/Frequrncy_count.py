def count_frequency(lst):
    character_count ={}
    for ch in lst:
        ch=ch.lower()
        if ch in character_count:
            character_count[ch]+=1
        else:
            character_count[ch]=1
    return character_count

ch_lst =['apple','banana','Orange']
print(count_frequency(ch_lst))