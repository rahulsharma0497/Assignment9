def permutations(s):
  """
  Prints all permutations of a given string.

  Args:
    s: A string.

  Returns:
    None.
  """

  if len(s) == 0:
    return
  else:
    for i in range(len(s)):
      permutations(s[0:i] + s[i + 1:])
      temp = s[i]
      s[i] = s[0]
      s[0] = temp


if __name__ == "__main__":
  s = "ABC"
  permutations(s)