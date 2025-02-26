class StringReverse:
    def rev_string(self,s):
        rev_str = ""
        for ch in s:
            rev_str = ch + rev_str
        return rev_str

rev = StringReverse()
s = input("Enter a String: ")
result = rev.rev_string(s)
print(f"{s}----> Reversed:-----> {result}")


rev_str = lambda s: ''.join(s[i]for i in range(len(s)-1,-1,-1))
print(rev_str(s))
