# Property Decorators :


class Car:

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def fullName(self):
        return f"the name is {self.__brand} {self.__model}"

    def model(self):
        return self.__model


MyCar = Car("tata", "Nexon")
MyCar.model="City"
print(MyCar.fullName())
# print(MyCar.model())
print(MyCar.model)
