# Encapsulation

# public : No underscore (e.g., self.name). Accessible everywhere.

# private:  Single underscore (e.g., self._name). Accessible within the class and subclasses; access from outside is discouraged but allowed.

# protected: Double underscore (e.g., self.__name). Python performs name mangling (internally renaming to _ClassName__name), making it harder but not impossible to access from outside the class.


class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    # getter method for brand
    def get_brand(self):
        return self.brand + " ! "

    def FullName(self):
        return f"The name is {self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def display(self):
        return f"The name is {self.brand} {self.model} and with battery size of  {self.batterySize}"


myElectricCar = ElectricCar("Mahindra", "XEV 9e", "79Kwh")

# print(myElectricCar.brand) #it will give error as brand is private and cant acces outside the class

print(myElectricCar.get_brand())
