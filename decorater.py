def decorate(func):
    def wrapper(*args,**kwargs):
        print("i am print before fumction")
        func(*args, **kwargs)
        print("i am print after function")
    return wrapper


@decorate
def add(*args):
    sum =0
    for i in args:
        sum =sum + i
    print(f"sum of you number is :{sum}")

add(12,12,22)