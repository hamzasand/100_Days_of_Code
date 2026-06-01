class Factory:
    a = "atribute from parent class"
    def show(self):
        print("function from parent class")

class FactoryFSD(Factory):
    def show(self):
        print("method from child class")


obj = FactoryFSD()
obj.show