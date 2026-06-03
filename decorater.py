def decorate(func):
    def wrapper(a,b):
        print("i am print before fumction")
        func(a,b)
        print("i am print after function")
    return wrapper


@decorate
def add(a,b):
    print(f"sum of you number is :{a+b}")

add(12,12)