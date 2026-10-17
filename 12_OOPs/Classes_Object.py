# Class: A blueprint for creating objects


# Syntax
class Car:
    # __init__ initializes object attributes
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


# Constructor (__init__):
# A special method called automatically when an object is created.

# self(this): yeah basicly connection establish krta hai function or class ka bich
# Refers to the current object and allows us to access its attributes.


# Creating objects:
# An object is an instance of a class.

my_Car1 = Car("Toyota", "Corolla")
my_Car2 = Car("Tata", "Safari")


# Accessing attributes
print(my_Car1.brand)
print(my_Car1.model)
print(my_Car2.brand)
print(my_Car2.model)


# example 2


class NewCar:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display(self):
        return f"The name is {self.brand} {self.model}"


my_Car1 = NewCar("Toyota", "Corolla")
my_Car2 = NewCar("Tata", "Safari")

print(my_Car1.display())
print(my_Car2.display())
