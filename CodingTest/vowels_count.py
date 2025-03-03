def vowels_count(s):
    vowels =['a','e','i','o','u','A','E','I','O','U']
    count =0
    for i in s:
        if i in vowels:
            count+=1
    return count
print(vowels_count('Halong Bayi'))