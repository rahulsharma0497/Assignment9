def factorial(n):
  """
  Returns the factorial of N.

  Args:
    n: An integer.

  Returns:
    The factorial of N.
  """

  if n < 0:
    raise ValueError("n must be a non-negative integer")
  if n == 0:
    return 1
  return n * factorial(n - 1)


if __name__ == "__main__":
  n = 5
  print(factorial(n))