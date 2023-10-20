def binary_search(array, target):
  """
  Searches for the target element in the sorted array.

  Args:
    array: A sorted list of elements.
    target: The element to be searched for.

  Returns:
    The index of the target element in the array, or -1 if the target element is not found.
  """

  low = 0
  high = len(array) - 1

  while low <= high:
    mid = (low + high) // 2

    if array[mid] == target:
      return mid
    elif array[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  return -1

