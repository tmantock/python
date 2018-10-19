# Matrix Class for implementing a classic Matrix
class Matrix(object):
    def __init__(self, matrix):
        """Class initializer
        
        Arguments:
            matrix {List[Integer]} -- The list of lists to use to create the matrix
        """

        self._container = matrix

    def __getitem__(self, key):
        """Method allows [] operator to be used for accessing an item
        
        Arguments:
            key {Integer} -- the list index
        
        Returns:
            List[Integer] -- the row of the matrix
        """

        return self._container[key]

    def __setitem__(self, key, value):
        """Method allows [] operator to be used for setting an index in the array
        
        Arguments:
            key {Integer} -- the list index
            value {List[Integer]} -- a row for the matrix
        """

        self._container[key] = value

    def __str__(self):
        """Method returns a string that can be used in print or str()
        
        Returns:
            String -- the string representation of a matrix
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
        """Method overrides the "*" operator
        
        Arguments:
            rhs {Matrix or Integer} -- the matrix or integer to multiply by
        
        Raises:
            ValueError -- The other object must be a matrix or an integer
        
        Returns:
            Matrix -- The resulting matrix
        """
        if type(rhs) is int:
            return [[x * rhs for x in row] for row in self._container]
        elif type(rhs) is Matrix:
            return self._multiply(rhs)
        
        raise ValueError("A Matrix can only be multiplied by a Matrix or an int")

    def __rmul__(self, lhs):
        """Method overrides the "*" operator
        
        Arguments:
            lhs {Matrix or Integer} -- the matrix or integer to multiply by
        
        Raises:
            ValueError -- The other object must be a matrix or an integer
        
        Returns:
            Matrix -- The resulting matrix
        """

        if type(lhs) is int:
            return [[x * lhs for x in row] for row in self._container]
        elif type(lhs) is Matrix:
            return self._multiply(lhs)
        
        raise ValueError("A Matrix can only be multiplied by a Matrix or an int")        

    def __add__(self, rhs):
        """Method overrides the "+" operator
        
        Arguments:
            rhs {Matrix} -- The other matrix
        
        Raises:
            ValueError -- Both objects must be matrix
            ValueError -- Both matrices must have the same size
        
        Returns:
            Matrix -- The resulting matrix
        """
        if type(rhs) is not Matrix:
            raise ValueError("Two Matrices are required for addition")
        elif self.size() != rhs.size():
            raise ValueError("Both Matrices must have the same size")
        
        return self._add(rhs)
    
    def __radd__(self, lhs):
        """Method overrides the "+" operator
        
        Arguments:
            lhs {Matrix} -- The other matrix
        
        Raises:
            ValueError -- Both objects must be matrix
            ValueError -- Both matrices must have the same size
        
        Returns:
            Matrix -- The resulting matrix
        """
        if type(lhs) is not Matrix:
            raise ValueError("Two Matrices are required for addition")
        elif self.size() != lhs.size():
            raise ValueError("Both Matrices must have the same size")
        
        return self._add(lhs, True)

    def __sub__(self, rhs):
        """Method overrides the "-" operator
        
        Arguments:
            rhs {Matrix} -- The other matrix
        
        Raises:
            ValueError -- Both objects must be matrix
            ValueError -- Both matrices must have the same size
        
        Returns:
            Matrix -- The resulting matrix
        """

        if type(rhs) is not Matrix:
            raise ValueError("Two Matrices are required for subtraction")
        elif self.size() != rhs.size():
            raise ValueError("Both Matrices must have the same size")
        
        return self._sub(rhs)
    
    def __rsub__(self, lhs):
        """Method overrides the "-" operator
        
        Arguments:
            lhs {Matrix} -- The other matrix
        
        Raises:
            ValueError -- Both objects must be matrix
            ValueError -- Both matrices must have the same size
        
        Returns:
            Matrix -- The resulting matrix
        """

        if type(lhs) is not Matrix:
            raise ValueError("Two Matrices are required for subtraction")
        elif self.size() != lhs.size():
            raise ValueError("Both Matrices must have the same size")
        
        return self._sub(lhs, True)

    def size(self):
        """Method returns the size of the matrix
        
        Returns:
            Tuple(Integer, Integer) -- a tuple containing the size (row, col)
        """

        return self._size(self._container)
    
    def is_empty(self):
        """Method checks if a Matrix is empty

        Returns:
            Boolean -- an indication if the matrix is empty
        """

        return self.size() == (0,0)

    def is_square(self):
        """Method returns a boolean indicating if the matrix is square
        
        Returns:
            Boolean -- indicate if the matrix is square
        """


        if (len(self._container)) == 0:
            return False

        return len(self._container) == len(self._container[0])


    def transpose(self):
        """Method transposes the matrix
        """

        if self.is_square():
            self._transpose_in_place()
            return
        
        self._container = self._transposed()

    def transposed(self):
        """Method returns a transposed version of the matrix
        
        Returns:
            Matrix -- the transposed matrix
        """

        return self._transposed()

    def determinant(self):
        """Method returns the determinant of a matrix
        
        Returns:
            Integer -- the determinant
        """


        if not self.is_square(): return

        return self._determinant(self._container)

    def _size(self, matrix):
        """Method helps to find the size of a matrix
        
        Arguments:
            matrix {Matrix} -- the matrix to work on
        
        Returns:
            Tuple(Integer, Integer) -- a tuple containing the size (row, col)
        """

        if len(matrix) == 0:
            return (0, 0)

        return (len(matrix), len(matrix[0]))

    def _transposed(self):
        """Method returns a transposed matrix
        
        Returns:
            List[List[Integer]] -- the transposed matrix lists
        """

        transposed, (rows, cols) = [], self.size()

        for i in range(cols):
            row = []
            for j in range(rows):
                row.append(self._container[j][i])
            transposed.append(row)
        
        return transposed
    
    def _transpose_in_place(self):
        """Mehtod transposes a matrix in place (the matrix must be square)
        """


        (rows, cols) = self.size()

        for i in range(rows):
            for j in range(i + 1, cols):
                self._container[i][j], self._container[j][i] = self._container[j][i], self._container[i][j]


    def _determinant(self, matrix):
        """Method helps to find the determinant of a matrix
        
        Arguments:
            matrix {Matrix} -- the matrix to work on
        
        Returns:
            Integer -- the determinant
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
        """Method multiplies the current Matrix with another Matrix.
        Order doesn't matter, since multiplication is commutative
        
        Arguments:
            rhs {Matrix} -- The matrix to multiply with
        
        Raises:
            ValueError -- Matrix size mismatch
        
        Returns:
            Matrix -- The Matrix resulting from multiplication
        """

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
        """Method returns the dot product of two arrays (Multiplying corresponding indices of the arrays and getting the sum of the products)
        
        Arguments:
            lhs {List[Integer]} -- The list of numbers
            rhs {List[Integer]} -- The list of numbers
        
        Returns:
            Integer -- The resulting dot product
        """

        product = 0

        if len(lhs) != len(rhs):
            return product
        
        for i in range(len(lhs)):
            product += lhs[i] * rhs[i]
        
        return product
    
    def _add(self, rhs, left = False):
        """Method adds two matrices together
        
        Arguments:
            rhs {Matrix} -- The other Matrix
        
        Keyword Arguments:
            left {bool} -- Flag indicating if the current Matrix is on the left hand side of the operator (order matters) (default: {False})
        
        Returns:
            Matrix -- The resulting Matrix
        """

        (rows, cols) = self.size()

        return Matrix([[rhs[i][j] + self._container[i][j] if left else self._container[i][j] + rhs[i][j] for j in range(cols)] for i in range(rows)])
    
    def _sub(self, rhs, left = False):
        """Method subtracts two matrices
        
        Arguments:
            rhs {Matrix} -- The other matrix
        
        Keyword Arguments:
            left {bool} -- Flag indicating if the current Matrix is on the left hand side of the operator (order matters) [description] (default: {False})
        
        Returns:
            Matrix -- The resulting Matrix from subtraction
        """

        (rows, cols) = self.size()

        return Matrix([[rhs[i][j] - self._container[i][j] if left else self._container[i][j] - rhs[i][j] for j in range(cols)] for i in range(rows)])

    def _get_column(self, index):
        """Method returns a vector of values for a column in a matrix
        
        Arguments:
            index {Integer} -- the column that should be returned
        
        Raises:
            ValueError -- Index out of range for the column specified in the matrix
        
        Returns:
            List[Integer] -- a vector of column values
        """

        if index >= self.size()[1]:
            raise ValueError("Index out of range for column")

        return [row[index] for row in self._container]

# Rotation Matrix Class
class RotationMatrix(Matrix):
    def x_vec(self):
        """Method returns a vector of the x axis values for the rotation matrix
        
        Raises:
            ValueError -- X axis values are missing from the matrix
        
        Returns:
            List[Integer] -- The vector of x-axis values
        """

        if self.is_empty() or self.size()[1] < 1:
            raise ValueError("No X Axis available")

        return self._get_column(0)

    def y_vec(self):
        """Method returns a vector of the y axis values for the rotation matrix
        
        Raises:
            ValueError -- Y axis values are missing from the matrix
        
        Returns:
            List[Integer] -- The vector of y-axis values
        """

        if self.is_empty() or self.size()[1] < 2:
            raise ValueError("No Y Axis available")

        return self._get_column(1)

    def z_vec(self):
        """Method returns a vector of the z axis values for the rotation matrix
        
        Raises:
            ValueError -- Z axis values are missing from the matrix
        
        Returns:
            List[Integer] -- The vector of z-axis values
        """

        if self.is_empty() or self.size()[1] < 3:
            raise ValueError("No Z Axis available")

        return self._get_column(2)
