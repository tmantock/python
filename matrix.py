# Matrix Class for implementing a classic Matrix
class Matrix(object):
    def __init__(self, matrix):
        """
        Initialzer

        @param matrix: A list of lists
        """
        self._container = matrix

    def __getitem__(self, key):
        """
        Method allows [] operator to be used for accessing an item

        @param key: The index of the matrix
        @return [Type]
        """
        return self._container[key]

    def __setitem__(self, key, value):
        """
        Method allows [] operator to be used for setting an index in the array

        @param key: the index of matrix
        @param value: the value to set to the index
        """
        self._container[key] = value

    def __str__(self):
        """
        Method returns a string that can be used in print or str()

        @return String
        """
        string = "[\n"

        for item in self._container:
            string += "[ "

            for i in item:
                string += str(i) + " "
            
            string += "]\n"
        
        string += "]"

        return string
    
    def __mul__(self, rhs):
        if type(rhs) is int:
            return [[x * rhs for x in row] for row in self._container]
        elif type(rhs) is Matrix:
            return self._multiply(rhs)
        
        raise ValueError("A Matrix can only be multiplied by a Matrix or an int")

    def __rmul__(self, lhs):
        if type(lhs) is int:
            return [[x * lhs for x in row] for row in self._container]
        elif type(lhs) is Matrix:
            return self._multiply(lhs)
        
        raise ValueError("A Matrix can only be multiplied by a Matrix or an int")        

    def __add__(self, rhs):
        if type(rhs) is not Matrix:
            raise ValueError("Two Matrices are required for addition")
        elif self.size() != rhs.size():
            raise ValueError("Both Matrices must have the same size")
        
        return self._add(rhs)
    
    def __radd__(self, lhs):
        if type(lhs) is not Matrix:
            raise ValueError("Two Matrices are required for addition")
        elif self.size() != lhs.size():
            raise ValueError("Both Matrices must have the same size")
        
        return self._add(lhs, True)

    def __sub__(self, rhs):
        if type(rhs) is not Matrix:
            raise ValueError("Two Matrices are required for subtraction")
        elif self.size() != rhs.size():
            raise ValueError("Both Matrices must have the same size")
        
        return self._sub(rhs)
    
    def __rsub__(self, lhs):
        if type(lhs) is not Matrix:
            raise ValueError("Two Matrices are required for subtraction")
        elif self.size() != lhs.size():
            raise ValueError("Both Matrices must have the same size")
        
        return self._sub(lhs, True)

    def size(self):
        """
        Method returns the size of the matrix

        @return (Int, Int)
        """
        return self._size(self._container)

    def is_square(self):
        """
        Method returns a boolean indicating if the matrix is square

        @return Boolean
        """

        if (len(self._container)) == 0:
            return False

        return len(self._container) == len(self._container[0])


    def transpose(self):
        if self.is_square():
            self._transpose_in_place()
            return
        
        self._container = self._transposed()

    def transposed(self):
        return self._transposed()

    def determinant(self):
        """
        Method returns the determinant of a matrix

        @return Int
        """

        if not self.is_square(): return

        return self._determinant(self._container)

    def _size(self, matrix):
        """
        Method helps to find the size of a matrix

        @return (Int, Int)
        """
        if len(matrix) == 0:
            return (0, 0)

        return (len(matrix), len(matrix[0]))

    def _transposed(self):
        transposed, (rows, cols) = [], self.size()

        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(self._container[j][i])
            transposed.append(row)
        
        return transposed
    
    def _transpose_in_place(self):
        """
        Method transposes the matrix in place
        """

        (rows, cols) = self.size()

        for i in range(rows):
            for j in range(i + 1, cols):
                self._container[i][j], self._container[j][i] = self._container[j][i], self._container[i][j]


    def _determinant(self, matrix):
        """
        Method helps to find the determinant of a matrix

        @return Int
        """

        if self._size(matrix) == (2, 2):
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

        determinant = 0
        first_row = matrix[0]

        for (index, element) in enumerate(first_row):
            temp_matrix = [[item for (i, item) in enumerate(row) if i != index] for row in matrix[1::]]

            if index % 2 == 0:
                determinant += element * self._determinant(temp_matrix)
            else:
                determinant -= element * self._determinant(temp_matrix)
        
        return determinant

    def _multiply(self, rhs):
        size_l = self.size()
        size_r = rhs.size()

        right, left, result = None, None, []

        if size_l[1] == size_r[0]:
            left, right = self, rhs
        elif size_l[0] == size_r[1]:
            left, right = rhs, self
        else:
            raise ValueError("The columns lenght of Matrix 1 must be the same as the row length of Matrix 2")
        
        right_transposed = right.transposed()

        for l_row in left:
            new_row = []

            for r_row in right_transposed:
                new_row.append(self._dot_product(l_row, r_row))
            
            result.append(new_row)
        
        return Matrix(result)
    
    def _dot_product(self, lhs, rhs):
        product = 0

        if len(lhs) != len(rhs):
            return product
        
        for i in range(len(lhs)):
            product += lhs[i] * rhs[i]
        
        return product
    
    def _add(self, rhs, left = False):
        (rows, cols) = self.size()

        return Matrix([[rhs[i][j] + self._container[i][j] if left else self._container[i][j] + rhs[i][j] for j in range(cols)] for i in range(rows)])
    
    def _sub(self, rhs, left = False):
        (rows, cols) = self.size()

        return Matrix([[rhs[i][j] - self._container[i][j] if left else self._container[i][j] - rhs[i][j] for j in range(cols)] for i in range(rows)])
