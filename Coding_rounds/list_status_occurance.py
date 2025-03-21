
def find_status_count(lst):
    status_count= {}
    for status in lst:
        if status in status_count:
            status_count[status]+=1
        else:
            status_count[status]=1
    return status_count

# output
status_lst =['PASS','FAIL','SKIP','PASS','PASS','FAIL']
result = find_status_count(status_lst)
print(f"Status count of the test cases are : {result}")