def my_decorator(func):
    def wrapper():
        print("Before Function call")
        func()
        print("After Function call")
    return wrapper

@my_decorator
def say_hello():
    print("Hello")

say_hello()