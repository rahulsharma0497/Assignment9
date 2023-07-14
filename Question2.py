def sum_of_first_n_natural_numbers(n):
  """
  Returns the sum of the first n natural numbers.

  Args:
    n: An integer.

  Returns:
    The sum of the first n natural numbers.
  """

  if n <= 0:
    return 0
  return n * (n + 1) // 2


if __name__ == "__main__":
  n = 3
  print(sum_of_first_n_natural_numbers(n))