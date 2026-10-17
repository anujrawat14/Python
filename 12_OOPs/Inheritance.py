# inheritance:

# syntax


class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"The name is {self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def display(self):
        return f"The name is {self.brand} {self.model} and with battery size of  {self.batterySize}"


myElectricCar = ElectricCar("Mahindra", "XEV 9e", "79Kwh")

print(myElectricCar.display())
