"""
Write a Python function to check if a given string is a valid email address. The function should:

Use regular expressions (re module) to validate the email format.

Return True if the email is valid and False otherwise.

"""
import re
def check_email(mail):
    valid_email = re.fullmatch('r^[a-zA-z0-9._]+@[a-zA-Z0-9._]+/.[a-zA-Z]{2,}$]',mail)
    if valid_email:
        return True
    else:
        return False

print(check_email("abcd_09@gmail.com"))