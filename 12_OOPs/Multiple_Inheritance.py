
# Multiple Inheritance : A  child class inherits from more than one parent class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def FullName(self):
        return f"The name is {self.brand} {self.model}"


class Battery:
    def Battery_info(self):
        return "This is battery"


class Engine:
    def Engine_info(self):
        return "This is Engine"


class ElectricCarTwo(Battery, Engine, Car):
    pass


myNewTesla = ElectricCarTwo("Tesla", "Model S")

print(myNewTesla.Battery_info())
print(myNewTesla.Engine_info())
print(myNewTesla.FullName())
