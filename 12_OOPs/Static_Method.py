# Static method : 


class Car:

    total_car = 0  # class variablr

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # self.total_car = self.total_car + 1
        Car.total_car += 1

    def FullName(self):
        return f"The name is {self.__brand} {self.model}"


Car1 = Car("Tata", "Xuv")