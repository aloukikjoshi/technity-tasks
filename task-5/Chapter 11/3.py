def divide_numbers(a, b):
    assert b != 0, "Division by zero is not allowed"
    result = a / b
    return result

try:
    quotient = divide_numbers(10, 0)
    print("The quotient is:", quotient)
except AssertionError as e:
    print("AssertionError:", e)
except Exception as e:
    print("An unexpected error occurred:", e)


# This code defines a Python program that contains a function divide_numbers(a, b) to perform division. Inside the function, it uses an assert statement to check if b is not equal to 0 to avoid division by zero. If b is 0, it raises an AssertionError with a specific message. The program then attempts to call the function with 10 and 0, triggering an AssertionError due to division by zero. It uses a try and except block to catch this AssertionError and prints a custom error message.
