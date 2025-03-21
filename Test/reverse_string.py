def rev_string(s):
     rev_str =""
     for ch in s:
         rev_str= ch+rev_str
     return rev_str
print(rev_string("Race"))

rev_strings = lambda s:''.join([s[i] for i in range(len(s)-1,-1,-1)])
print(rev_strings("Program"))