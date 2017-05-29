def compare_list(arrA, arrB):
    if len(arrA) != len(arrB):
        return 0
    
    i = 0
    x = 0
    y = 0

    while y < len(arrA):
        i += 1
        print "Iter %d" %i

        if(arrA[y] == arrB[x]):
            print arrA[y]
            y += 1
            x += 1
        elif(arrA[y] < arrB[x]):
            y += 1
        elif(arrA[y] > arrB[x]):
            x += 1

                
arrA = [13, 27, 35, 40, 49, 55, 59]
arrB = [17, 35, 39, 40, 55, 58, 60]

compare_list(arrA, arrB)