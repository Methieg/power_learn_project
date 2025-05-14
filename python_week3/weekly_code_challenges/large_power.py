#!/bin/python3
def large_power(base, exponent):
  """
  Tests if the result of base raised to the power of exponent is greater than 5000.

  Args:
    base: The base number.
    exponent: The exponent to which the base is raised.

  Returns:
    True if the result is greater than 5000, False otherwise.
  """
  result = base ** exponent
  if result > 5000:
    return True
  else:
    return False

