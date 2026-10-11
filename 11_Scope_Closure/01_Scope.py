# =========================
# Global and Local Scope
# =========================

# username = "chaiAurCode"
#
# def func():
#     username = "chai"
#     print(username)
#
# print(username)  # Output: chaiAurCode
# func()           # Output: chai


# =========================
# Example 1: Accessing a Global Variable
# =========================

username = "chaiAurCode"

def func():
    # No local variable named username exists.
    # Python looks in the enclosing scopes and then the global scope.
    print(username)

print(username)  # Output: chaiAurCode
func()           # Output: chaiAurCode

# Note:
# A function can read a global variable if no local variable
# with the same name shadows it.
# Reading a global variable does not cause an error.


# =========================
# Example 2: Using a Global Variable
# =========================

x = 99

def func2(y):
    # x is read from the global scope.
    z = x + y
    return z

result = func2(1)
print(result)  # Output: 100


# =========================
# Example 3: Modifying a Global Variable
# =========================

var1 = 99

def func3():
    # The global keyword tells Python to modify the global var1,
    # instead of creating a local variable named var1.
    global var1
    var1 = 88

    # Avoid changing global variables inside functions when possible.
    # It can make code harder to understand and maintain.

func3()
print(var1)  # Output: 88


# =========================
# Example 4: Local and Enclosing Scope (Nested Functions)
# =========================

x = 99

def func4():
    x = 88  # Local variable belonging to func4.

    def func5():
        # Python finds x in the enclosing scope (func4).
        print(x)  # Output: 88

    func5()

func4()

# Note:
# The local x inside func4 shadows the global x = 99
# when Python looks up x inside func5.