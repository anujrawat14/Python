# Property Decorators : @property is a decorator that allows you to access a method like an attribute, without using parentheses ().


class Car:

    def __init__(self, brand, model):
        self.__brand = brand
        self.__model = model

    def fullName(self):
        return f"the name is {self.__brand} {self.__model}"

    @property
    def model(self):
        return self.__model


MyCar = Car("tata", "Nexon")

# MyCar.model="City" # This will raise an AttributeError

print(MyCar.fullName())

# print(MyCar.model()) #model is now accessed like an attribute(property)
print(MyCar.model)
