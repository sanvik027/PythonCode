list1= [1,2,3]
list2 =['a','b','c']

zipped = zip(list1,list2)

zipped_list = list(zipped)

print(zipped_list)

names = ['Alice','Bob','Tim','Cook']
marks = [80,38,90,78]
score_dict = dict(zip(names,marks))
print(score_dict)

pairs= [(1,'a'),(2,'b'),(3,'c')]
numbers, letters = zip(*pairs)
print(numbers)
print(letters)