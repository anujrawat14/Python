#  polymorphism :it allows different classes to use the same interface or method name, but execute different, class-specific behaviors.
class Car:
    def __init__(self, brand, model):
        self.brand = brand  
        self.model = model  

    def fuel_type(self):
        return "petrol or diesel"

    def FullName(self):
        return f"The name is {self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def display(self):
        return f"The name is {self.get_brand()} {self.model} and with battery size of {self.batterySize}"

    def fuel_type(self):
        return "battery charge"


myElectricCar = ElectricCar("Mahindra", "XEV 9e", "79Kwh")
myCar = Car("Tata", "Nexon")

print(myCar.fuel_type())
print(myElectricCar.fuel_type())
