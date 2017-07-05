def quickSort(arr, left, right):
    if left >= right:
        return
    # Pick a position to pivot from
    pivot = arr[(left + right) / 2]
    # Get index to divide the list for a divide and conquer for quicksort
    # Partition handles swapping the indexes
    index = partition(arr, left, right, pivot)
    print "Partition %d" %index
    print "&&&&&&&&&&&&&&&&&&&"
    # Sort everything left of the index returned from the partition
    quickSort(arr, left, index - 1)
    # Sort everything right of the index returned from the partition
    quickSort(arr, index, right)

def partition(arr, left, right, pivot):
    while left <= right:
        # Make sure all elements to the left of the pivot are less than it
        # If the element is less than pivot then move the left indicator over to the right
        # Don't move the pivot if the element is greater than the pivot. Target it for a swap
        while arr[left] < pivot:
            left += 1
        # Make sure all elements to the right of the pivot are greater than the pivot
        # If the element is greater than the pivot, then move the indicator for right to the left
        # Don't move the pivot if the element is less than the pivot. Target for a swap
        while arr[right] > pivot:
            right -= 1
        # If the left is less than or equal to the right, swap the elements
        # From the previous while loops this indicated that there are elements before the pivot
        # that are greater that it, and elements to the left of the pivot that are less than it
        # These elemts should be swapped and the left incremented and right decremented to reflect
        # reflect the swap and handle condition for parent while loop to exit
        if left <= right:
            print "Pivot %d" %pivot
            print "Left %d" %left
            print "Right %d" %right
            print arr
            print "--------------"
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left

arr = [5,6,8,2,3,7,9,1,4]
quickSort(arr, 0, len(arr) - 1)
print arr