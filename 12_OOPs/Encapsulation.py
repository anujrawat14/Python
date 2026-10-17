
# Encapsulation : Bundling data (attributes) and methods into a class.

# public: No underscore (e.g., self.name). Accessible everywhere.

# protected: Single underscore (e.g., self._name).
# Accessible within the class and subclasses; outside access is discouraged but allowed.

# private: Double underscore (e.g., self.__name).
# Python performs name mangling (internally renaming it to _ClassName__name),
# making it harder, but not impossible, to access from outside the class.


class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.model = model    # Public attribute

    # Getter method for brand
    def get_brand(self):
        return self.__brand + " ! "

    def set_brand(self,brand):
        self.__brand=brand

    def FullName(self):
        return f"The name is {self.__brand} {self.model}"


class ElectricCar(Car):
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def display(self):
        return f"The name is {self.get_brand()} {self.model} and with battery size of {self.batterySize}"


myElectricCar = ElectricCar("Mahindra", "XEV 9e", "79Kwh")

# print(myElectricCar.__brand)  # Error: private attribute uses name mangling
print(myElectricCar.set_brand("Tesla"))

print(myElectricCar.get_brand())
