# =========================
# Closure in Python :# it dont send only definiton of function it also send the variable related to the definition of function 
# =========================

x = 99

def f1():
    x = 88

    def f2():
        # f2 remembers the variable x from the enclosing scope of f1.
        print(x)

    # Returning the inner function along with access to its enclosing variables.
    return f2

myResult = f1()
myResult()  # Output: 88


# =========================
# Example: Closure as a Function Factory
# =========================

def chaiCode(num):
    def actual(x):
        # The inner function remembers num from chaiCode's enclosing scope.
        return x ** num

    # Return the inner function with access to num.
    return actual

myRes = chaiCode(3)

# Check the type of the returned object (a function).
# print(type(myRes))

print(myRes(2))  # Output: 8 (2 ** 3)