# Exception Handling in Python

## Basic Syntax


try:
    # Code that might cause an error
    pass

except Exception as e:
    # Code to handle the error
    print(e)


## Example 1: Basic try-except

# try-except: Used for exception handling

try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)

except Exception as e:
    # Handles an exception and prints the error message
    print("An error occurred:", e)


## Example 2: Specific Exceptions and finally


try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(result)

except ValueError:
    # Executes if the input cannot be converted to an integer
    print("Please enter a valid integer.")

except ZeroDivisionError:
    # Executes if the program attempts to divide by zero
    print("Cannot divide by zero.")

finally:
    # Executes whether an exception occurs or not
    print("Program execution completed.")
