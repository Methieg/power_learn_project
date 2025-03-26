#!/usr/bin/python3
def calculator():

    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

        sign = input("Choose operation: +, - ,/, *: ")

        match (sign):
            case '+':
                return (a + b)
            case '-':
                return (a -b)
            case '*':
                return (a * b)
            case '/':
                if b == 0:
                    return "Cannot divide by zero"
                return (a / b)
            case _:
                return "Error: Invalid operation"
    except ValueError:
        return "Error: Invalid input.Numbers only are allowed"

result = calculator()
print("Result: ", result)
                       
