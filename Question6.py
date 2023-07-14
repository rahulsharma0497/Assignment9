def nth_term_of_arithmetic_progression(a, d, n):
  """
  Returns the Nth term of the arithmetic progression series.

  Args:
    a: The first term of the arithmetic progression series.
    d: The common difference of the arithmetic progression series.
    n: The Nth term of the arithmetic progression series.

  Returns:
    The Nth term of the arithmetic progression series.
  """

  if n == 1:
    return a
  else:
    return nth_term_of_arithmetic_progression(a + d, d, n - 1)


if __name__ == "__main__":
  a = 2
  d = 1
  n = 5
  print(nth_term_of_arithmetic_progression(a, d, n))