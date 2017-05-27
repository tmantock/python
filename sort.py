# Binary Search through recursion
# assumes the list has been sorted


def binary_search(array, n):
    mid = len(array) / 2

    if n == array[mid]:
        return array[mid]

    if n > array[mid]:
        b = array[mid:]
    if n < array[mid]:
        b = array[:mid]

    return binary_search(b, n)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20]

print binary_search(arr, 6)
