
def repeat_last_character(word, i):
    return word[0:len(word)-1]+((word[-1]) * i)

text = input("Enter the word : ")
times = int(input("How many times do you want to repeat : "))
print(repeat_last_character(text,times))


def repeat_each_character(word,i):
    result =""
    for n in word:
        result = result + n*i
    return result
text = input("Enter the word : ")
times = int(input("How many times do you want to repeat : "))
print(repeat_each_character(text,times))


