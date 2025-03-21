""""
Write a Python function that:

Simulates a login scenario where you validate usernames and passwords from a given dictionary.

The dictionary contains usernames as keys and passwords as values (e.g., {"user1": "pass123", "user2": "qwerty", "admin": "admin123"}).

Ask the user to input a username and password, then check if the credentials are correct.

Display a success message for valid credentials and an error message otherwise.
"""


def validate_login(users):
    # input prompt
    user_name = input("Please Enter the Username: ")
    password = input("Please Enter the Password: ")

    # check if the username exist on the dictionary:
    if user_name in users:
        # validate password
        if users[user_name] == password:
            print("Login successful! Welcome,", user_name)
        else:
            print("Error: Invalid password.")
    else:
        print("Error: Username not found.")

    # Example usage


user_credentials = {
    "user1": "pass123",
    "user2": "qwerty",
    "admin": "admin123"
}

validate_login(user_credentials)