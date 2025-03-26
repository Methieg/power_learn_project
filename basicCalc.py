#!/bin/python3
def calculator(a, b):
  a = int(input("Enter first number: "))
  b = int(input("Enter second number: "))

  sign = input("Choose operation: +, - ,/, *")

  match (sign):
    case '+':
      return (a + b)
    case '-':
      return (a -b)
    case '*':
      return (a * b)
    case '/':
      return (a / b)
