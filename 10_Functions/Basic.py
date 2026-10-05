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
