def find_spiral(matrix):    
    spiral_list = []
    if matrix == None or len(matrix) == 0:
        return list
    m = len(matrix) 
    n = len(matrix[0])
    x=0
    y=0

    while(m>0 and n>0):
        if(m==1):
            i = 0
            while i < n:
                spiral_list.append(matrix[x][y])
                i += 1
                y += 1
            break
        elif(n==1):
            i = 0
            while i < m:
                spiral_list.append(matrix[x][y])
                i += 1
                x += 1
            break

        i = 0
        while i < n-1:
            spiral_list.append(matrix[x][y])
            i+=1
            y+=1
        
        j = 0
        while j < m-1:
            spiral_list.append(matrix[x][y])
            j+=1
            x+=1
        
        i = 0
        while i < n-1:
            spiral_list.append(matrix[x][y])
            i+=1
            y-=1

        j = 0
        while j < m-1:
            spiral_list.append(matrix[x][y])
            j+=1
            x-=1
        
        x+=1
        y+=1
        m=m-2
        n=n-2

    return spiral_list
