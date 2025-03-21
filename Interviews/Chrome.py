


class BaseDriver:
    def initialize_driver(self):
        print("intilizing base driver")


class ChromeDriver(BaseDriver):
    def initialize_driver(self):
        print("intilizing Chrome Driver")


driver = ChromeDriver()
driver.initialize_driver()



def disp_logs(func):
    def wrapper(*args, **kwargs):
        print(f"Calling the function: {func.__name__}")
        result = func(*args, **kwargs)
        print("Function called successfully")
        return result
    return wrapper

@disp_logs
def say_hello(name):
    return f"Hello!!! {name}"

print(say_hello("Vikii"))
