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

# example
x=99
def func2():
    z=x+y
    return z

result=func2(1)

print(result)
