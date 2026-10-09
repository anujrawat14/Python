import math


def Func(radius):
    pi = math.pi
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference


area,circumference=Func(5)
print("Area of circle is :",round(area,2))
print("Parameter of circle is :",round(circumference,2))
