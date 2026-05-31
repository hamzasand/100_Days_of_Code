class FactoryLahore:
    var = "Am variable from parente class or super class"
    def hello(self):
        print("Hello am method from super class")

class FactoryFaisalabad(FactoryLahore):
    pass

obj = FactoryLahore()
print(obj.var)

obj2 = FactoryFaisalabad()
print(obj2.var)
obj2.hello()