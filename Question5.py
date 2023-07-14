def find_max_element(arr, n):
  """
  Returns the maximum element of arr.

  Args:
    arr: An array of integers.
    n: The length of arr.

  Returns:
    The maximum element of arr.
  """

  if n == 0:
    return None
  else:
    max_element_so_far = find_max_element(arr, n - 1)
    if max_element_so_far is None:
      return arr[n - 1]
    else:
      return max(max_element_so_far, arr[n - 1])


if __name__ == "__main__":
  arr = [1, 4, 3, -5, -4, 8, 6]
  n = len(arr)
  print(find_max_element(arr, n))