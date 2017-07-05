def quickSort(arr, left, right):
    if left >= right:
        return
    pivot = arr[(left + right) / 2]
    index = partition(arr, left, right, pivot)
    quickSort(arr, left, index - 1)
    quickSort(arr, index, right)

def partition(arr, left, right, pivot):
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left

arr = [2,3,4,5,6,7,9,1,4]
quickSort(arr, 0, len(arr) - 1)
print arr