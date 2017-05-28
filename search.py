# Binary Search through recursion
# assumes the list has been sorted


def binary_search(haystack, needle):
    if needle > haystack[-1] or needle < haystack[0]:
        return "Out of Bounds"

    mid = len(haystack) / 2

    if needle == haystack[mid]:
        return haystack[mid]
    elif needle > haystack[mid]:
        h = haystack[mid:]
    elif needle < haystack[mid]:
        h = haystack[:mid]
    return binary_search(h, needle)

def binary_search_while(haystack, needle):
    if needle > haystack[-1] or needle < haystack[0]:
        return "Out of Bounds"
    go = True

    while go:
        mid = len(haystack) / 2

        if needle == haystack[mid]:
            go = False
            return haystack[mid]
        elif needle > haystack[mid]:
            haystack = haystack[mid:]
        elif needle < haystack[mid]:
            haystack = haystack[:mid]

arr = range(1,100000)

print binary_search_while(arr, 55)
print binary_search(arr, 55)
