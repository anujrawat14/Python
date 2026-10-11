def chaiCode(num):
    def actual(x):
        return x**num
    return actual

myres=chaiCode(3)
# print(type(myres))
print(myres(2))