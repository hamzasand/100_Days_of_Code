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
        print(f"so human name and is : {self.name}, {self.age}")


animal1 = Animal("hamza")
human1 = Human("hamza", 28)

animal1.show()
human1.show()