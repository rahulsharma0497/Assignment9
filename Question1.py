def is_power_of_two(n):
  """
  Returns true if n is a power of two, otherwise false.

  Args:
    n: An integer.

  Returns:
    True if n is a power of two, otherwise false.
  """

  if n <= 0:
    return False
  while n % 2 == 0:
    n >>= 1
  return n == 1


if __name__ == "__main__":
  n = 1
  print(is_power_of_two(n))