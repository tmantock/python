# Binary Search through recursion
# assumes the list has been sorted


def binary_search(haystack, needle):
    mid = len(haystack) / 2

    if needle == haystack[mid]:
        return haystack[mid]
    elif needle > haystack[mid]:
        h = haystack[mid:]
    elif needle < haystack[mid]:
        h = haystack[:mid]

    return binary_search(h, needle)

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 18, 19, 20]

print binary_search(arr, 6)
