arr = [12, 35, 1, 10, 34, 1]
sorted_arr = sorted(arr)
print(arr[-2])
max=[]
for i in range(0,len(arr)-1):
    for j in range(i+1):
        if arr[i] > arr[j]:
            max =arr[i]

print(max)
a=[1,3,5]
b=[2,4,6]
a.extend(b)


