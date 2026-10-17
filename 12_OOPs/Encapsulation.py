# Encapsulation

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def FullName(self):
        return f"The name is {self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        #super : Accesses the parent class implementation through Python's method resolution order
        super().__init__(brand, model)
        self.batterySize = batterySize

    def display(self):
        return f"The name is {self.brand} {self.model} and with battery size of  {self.batterySize}"

