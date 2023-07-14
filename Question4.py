def power(n, p):
  """
  Returns N^P.

  Args:
    n: An integer.
    p: An integer.

  Returns:
    N^P.
  """

  if p < 0:
    raise ValueError("p must be a non-negative integer")
  if p == 0:
    return 1
  if p == 1:
    return n
  return n * power(n, p - 1)


if __name__ == "__main__":
  n = 5
  p = 2
  print(power(n, p))