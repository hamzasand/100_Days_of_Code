class Animal:
    a = "a attribute from parent class with public variable"
    _a = "a attribute from parent class with protected variable"
    __a = "a attribute from parent class with private variable"
    def show(self):
        print("a message from parent class")

obj = Animal()
print(obj.a)
print(obj._a)
print(obj.__a)