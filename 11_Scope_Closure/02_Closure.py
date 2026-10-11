
x=99

def f1():
    x=88
    def f2():
        print(x)
    return f2

myResult=f1()
myResult()

# it dont send only definiton of function it also send the variable related to the definition of function call as closure

# example 

def chaiCode(num):
    def actual(x):
        return x**num
    return actual

myRes=chaiCode(3)
# print(type(myres))
print(myRes(2))