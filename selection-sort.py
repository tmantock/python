
def selSort(L):
    """Assumes that L is a list of elements that can be compared
       using >.  Sorts L in ascending order"""
    for i in range(len(L) - 1):
        #Invariant: the list L[:i] is sorted
        minIndx = i
        minVal= L[i]
        j = i + 1
        while j < len(L):
            if minVal > L[j]:
                minIndx = j
                minVal= L[j]
            j += 1
        temp = L[i]
        L[i] = L[minIndx]
        L[minIndx] = temp
        print 'Partially sorted list =', L

L = [35, 4, 5, 29, 17, 58, 0]
selSort(L)
print 'Sorted list =', L
