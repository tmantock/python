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
        """
        Method transposes the matrix in place
        """

        rows, cols = len(self._container), len(self._container[0])

        for i in range(rows):
            for j in range(i + 1, cols):
                self._container[i][j], self._container[j][i] = self._container[j][i], self._container[i][j]

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
