# function : A function is a reusable block of code that performs a specific task.

# creating a function : A function is created using the def keyword.It is also called definition of function


def greet():
    print("Hello, ANUJ")


#  calling a function : Defining a function does not execute its code.We have to call the function to execute it.
greet()


# function with parameter:A parameter is a variable written inside the parentheses while defining a function.
def greet(name):
    print("hello  ", name)


# argument:The actual value passed when calling the function
greet("Hitesh")

# function with return :return sends a value back to the place where the function was called.


def add(a, b):
    return a + b


result = add(2, 3)
print(result)


# Default Parameter :A default parameter has a default value.


def greet(name="Anuj"):
    print("good Night ", name)


greet()
greet("hitesh")


# *args: It allows a function to accept multiple positional arguments,collects the arguments into a tuple.


def numbers(*num):
    print(num)


numbers(1, 2, 3)

# **kwargs: It allows a function to accept multiple keyword arguments and collects keyword arguments into a dictionary.

def student(**details):
    print(details)

student(name="Anuj", age=21, branch="CSE")


# lambda function : A lambda is a small anonymous function,without name and define  using  lambda keyword 

out=lambda x:print(x)
out(10)

add =lambda a,b: a+b
print(add(19,1))