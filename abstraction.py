from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def parameter(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Square(Abstract):
    def __init__(self,side):
        self.side = side

    def parameter(self):
        print("ihave created parameters")

    def area(self):
        print("i have calculate the area")
  
obj = Square(7)
obj.area()
obj.parameter()