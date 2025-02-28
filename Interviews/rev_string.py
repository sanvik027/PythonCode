rev_string = lambda s: ''.join((s[i] for i in range(len(s)-1,-1,-1)))
print(rev_string("Hello_World"))

lst =[1,2,3,4,5,6,7,8,9,10]
even_lst =[x for x in lst if x %2 == 0]
print(even_lst)

"""with open("file.txt",'w') as r:
	r.write("some text")"""
