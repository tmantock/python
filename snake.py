def find_spiral(matrix):    
    output = []
    
    while matrix:
        row = matrix.pop(0)
        output.extend(row)
        matrix = zip(*matrix)[::-1]
    return output
