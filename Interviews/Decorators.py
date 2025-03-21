# declaring a decorator function
import logging
logging.basicConfig(level=logging.INFO)


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Pass the parameter to see the greetings :")
        result = func(*args,**kwargs)
        print("Function executed successfully:")
        return result
    return wrapper

# calling the decorator
@my_decorator
def greet(msg):
    return f"hello {msg}!!!!"

# output
print(greet("Ram"))


