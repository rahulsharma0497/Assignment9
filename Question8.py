def product_of_array_elements(arr, n):
  """
  Returns the product of all array elements.

  Args:
    arr: An array of integers.
    n: The length of arr.

  Returns:
    The product of all array elements.
  """

  if n == 0:
    return 1
  else:
    return arr[0] * product_of_array_elements(arr[1:], n - 1)


if __name__ == "__main__":
  arr = [1, 2, 3, 4, 5]
  n = len(arr)
  print(product_of_array_elements(arr, n))