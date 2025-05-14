#!/bin/python
def divisible_by_ten(num):
  """
  Determines whether or not a number is divisible by ten.

  Args:
    num: The number to check for divisibility.

  Returns:
    True if num is divisible by 10, False otherwise.
  """
  remainder = num % 10
  if remainder == 0:
    return True
  else:
    return False

