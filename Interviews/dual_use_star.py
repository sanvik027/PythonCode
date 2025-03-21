def greet(*args):
    for name in args:
        print(f"Hello: {name}")

greet(['Ram','Sita','Laxman'])

def disp_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}: {value}")
info = {"name": "Alice", "age": 30, "city": "Paris"}
disp_info(**info)
