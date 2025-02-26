def rev_string(name):
    """

    :param name: String as input
    :return: reverse of the string
    """
    return name[::-1]

name = input("Please enter the name: ")
print(f"The reverse of {name} is : {rev_string(name)}")

name = "Chiranjibi"
rev_name= str()

for n in name:
    rev_name= n+rev_name
print(rev_name)