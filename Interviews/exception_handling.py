


def divide_num(a,b):

    try:
        return a/b
    except Exception as e:
        print(f'Exception occurred : {e}')


print(divide_num(3,0))
