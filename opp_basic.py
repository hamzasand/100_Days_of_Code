class Factory:
    def __init__(self,material,zip,pocket):
        self.material = material
        self.zip = zip
        self.pocket = pocket
    

    def show(self):
        print(f"{self.material}, {self.zip}, {self.pocket}")

rebook = Factory("leather",2,4)  # object of class
rebook.show() # via object excess the method


