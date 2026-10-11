# username="chaiAurCode"

# def func():
#     username="chai"
#     print(username)


# print(username)
# output: chaiAurCode
# func()
# output: "chai"

username = "chaiAurCode"


def func():
    # username = "chai"
    print(username)


print(username)
# if variable is global then it wieill give error
func()
# if  variable is not present locally but present globbaly so it
# will give  same as globally variable

# example 1

x=99

def func2(y):
    z=x+y
    return z

result=func2(1)

print(result)

# example 2

var1=99

def func3():
    global var1
    var1=88

func3()
print(var1)