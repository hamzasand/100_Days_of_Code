class Animal:
    a = "a attribute from parent class"
    def show(self):
        print("a message from parent class")

obj = Animal()
print(obj.a)