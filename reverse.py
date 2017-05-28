def reverse(array):
    if len(array) == 0:
        return 0

    last = len(array) - 1

    for i in range(len(array)/2):
        temp = array[i]
        array[i] = array[last]
        array[last] = temp
        last -= 1

arr = range(1,100)

print arr

reverse(arr)

print arr
