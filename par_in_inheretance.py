class Animal:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"hello animal name is:{self.name}")

class Human(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def show(self):
        print(f"so human name and is : {self.nam}, {self.age}")