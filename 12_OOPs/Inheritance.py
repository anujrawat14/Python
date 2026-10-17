# inheritance: Inheritance allows a child class to reuse the attributes and methods of a parent class without writing them again.

# syntax : child(parent)


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


myElectricCar = ElectricCar("Mahindra", "XEV 9e", "79Kwh")

print(myElectricCar.display())
print(myElectricCar.FullName())
