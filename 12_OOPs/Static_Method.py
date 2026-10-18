# Static method : A static method is a function defined within a class that belongs to the class itself rather than any specific instance of that class


class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def FullName(self):
        return f"The name is {self.__brand} {self.model}"

    # If you don't use @staticmethod, Python treats general_description() as a regular instance method.

    @staticmethod
    def general_description():
        return f"Cars are mean of transport"


Car1 = Car("Tata", "Xuv")
# print(Car1.general_description()) #Raises a TypeError because Python automatically passes Car1 as the first argument, but the method accepts no arguments.

print(Car1.general_description())
print(Car.general_description())


 