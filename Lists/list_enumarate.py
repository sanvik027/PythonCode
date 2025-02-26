import random

fruits=['apple','banana','cherry']
for index,fruit in enumerate(fruits,start=1):
    print(f"{index}:{fruit}")

words = "Python"

for index, letters in enumerate(words):
    print(index,letters)

num_list = [random.randint (1,100) for _ in range(10)]
even_list = [n for index,n in enumerate(num_list) if n%2 == 0]
print(even_list)
names =['Alice','Bob','Mark']
marks = [85,70,34]
for index,(name,score)in enumerate(zip(names,marks)):
    print(f"{index},{name},{score}")