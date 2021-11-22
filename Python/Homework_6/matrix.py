class Matrix:
    def __init__(self, *args, **kwargs):
        """
        Takes 2 keyword arguments: filename or list. If filename is given
        read the matrix from file. Else, read it directly from list.
        """
        if 'filename' in kwargs:
            self.read_from_file(kwargs['filename'])
        elif 'list' in kwargs:
            self.read_as_list(kwargs['list'])


    def read_as_list(self, matrix_list):
        if len(matrix_list) == 0:
            self._matrix = []
            self._columns = 0
            self._rows = 0
            return

        columns_count_0 = len(matrix_list[0])
        if not all(len(row) == columns_count_0 for row in matrix_list):
            raise ValueError('Got incorrect matrix')

        self._matrix = matrix_list
        self._rows = len(self._matrix)
        self._columns = columns_count_0


    def read_from_file(self, filename):
        with open(filename, 'r') as f:
            matrix_list = f.readlines()
        matrix_list = list(map(lambda s: list(map(float, s[:-1].split(' '))), matrix_list))
        self.read_as_list(matrix_list)


    def __str__(self):
        s = '---------MATRIX---------\n'
        s += '\n'.join(str(row) for row in self._matrix)
        s += '\n'
        s += f'colums = {self.shape[0]}\nrows = {self.shape[1]}'
        s += '\n------------------------\n'
        return s


    def write_to_file(self, filename):
        """
        Write the matrix to the given filename.
        """
        with open(filename, 'w') as f:
            f.writelines(str(row)+'\n' for row in self._matrix)


    def traspose(self):
        """
        Transpose the matrix.
        """
        rows = self._rows
        cols = self._columns

        # Create a new/3rd empty matrix
        tpos_mat = Matrix( list = [ [0.0] * cols for i in range(rows) ] )

        for i in range(cols):
            for j in range(rows):
                tpos_mat._matrix[i][j] = self._matrix[j][i]

        return tpos_mat


    @property
    def shape(self):
        return self._columns, self._rows


    def __add__(self, other):
        """
        The `+` operator. Sum two matrices.
        Columns and rows sizes of two matrices should be the same.

        If other is not a matrix (int, float) add other to all elements of the matrix.
        """
        # Create a new/3rd empty matrix
        mat_3 = Matrix( list = [ [0.0] * self._columns for i in range(self._rows) ] )

        # Check if the other object is of type Matrix
        if isinstance (other, Matrix):
            if self._columns != other._columns or self._rows != other._rows :
                raise ValueError('Got incorrect matrices: dimensions are not equal')
            else:
                # Add the corresponding element of the self and other matrices
                for i in range(self._rows):
                    for j in range(self._columns):
                        mat_3._matrix[i][j] = self._matrix[i][j] + other._matrix[i][j]

        # If the other object is a scaler
        elif isinstance (other, (int, float)):
        	# Add that constant to every element of the self matrix
        	for i in range(self._rows):
        		for j in range(self._columns):
        			mat_3._matrix[i][j] = self._matrix[i][j] + other

        return mat_3


    # Addition (pointwise) is commutative
    def __radd__(self, other):
        return self.__add__(other)


    def __mul__(self, other):
        """
        The `*` operator: Pointwise/Element-wise matrix multiplication.
        Columns and rows sizes of two matrices should be the same.

        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        """

        # Create a new/3rd empty matrix
        mat_3 = Matrix( list = [ [0.0] * self._columns for i in range(self._rows) ] )

        # Check if the other object is of type Matrix
        if isinstance (other, Matrix):
            # Check the dimensions
            if self._columns != other._columns or self._rows != other._rows :
                raise ValueError('Got incorrect matrices: dimensions are not equal')
            else:
                # Multiply the corresponding elements of the self and other matrices
                for i in range(self._rows):
                    for j in range(self._columns):
                        mat_3._matrix[i][j] = self._matrix[i][j] * other._matrix[i][j]

        # If the other object is a scaler
        elif isinstance (other, (int, float)):
        	# Multiply that constant to every element of the self matrix
        	for i in range(self._rows):
        		for j in range(self._columns):
        			mat_3._matrix[i][j] = self._matrix[i][j] * other

        return mat_3


    # Point-wise multiplication is also commutative
    def __rmul__(self, other):
        return self.__mul__(other)


    def __matmul__(self, other):
        """
        The `@` operator. Mathematical matrix multiplication.
        The number of columns in the 1st (self) matrix must be equal to the number of rows in the 2nd (other) matrix.

        If other is not a matrix (int, float) multiply all elements of the matrix to other.
        """

        # Check if the other object is of type Matrix
        if isinstance (other, Matrix):
            # Check the dimensions
            if self._columns != other._rows:
                raise ValueError('Got incorrect matrices: dimensions are not suitable for multiplication')
            else:
                # Create a new/3rd empty matrix
                mat_3 = Matrix( list = [ [0.0] * other._columns for _ in range(self._rows) ] )

                #  Multiply the elements in the same row of the 1st matrix 
			    # to the elements in the same column of the 2nd matrix
                for i in range(self._rows):
                    for j in range(other._columns):
                        acc_sum = 0
                        # Note: self._columns == other._rows
                        for k in range(other._rows):
                            acc_sum += self._matrix[i][k] * other._matrix[k][j]

                        mat_3._matrix[i][j] = acc_sum
                
                return mat_3

        # If the other object is a scaler
        elif isinstance (other, (int, float)):
        	# Multiply that constant to every element of the self matrix
            return self.__mul__(other)

        
    @property
    def trace(self):
        """
        Check if the matrix is square, find the trace of the matrix.
        """

        # Check if the self object is of type Matrix
        if isinstance (self, Matrix):
            # Check the dimensions
            if self._columns != self._rows:
                raise ValueError('Got incorrect matrices: dimensions are not equal (not a square matrix)')
            else:
                trace_sum = 0
                # The trace of a square matrix is the sum of its diagonal elements.
                for i in range(self._rows):
                    trace_sum += self._matrix[i][i]

            return trace_sum


    @property
    def determinant(self):
        """
        Check if the matrix is square, find the determinant.
        TODO: implement
        """

        # # Check if the self object is of type Matrix
        # if isinstance (self, Matrix):
        #     # Check the dimensions
        #     if self._columns != self._rows:
        #         raise ValueError('Got incorrect matrices: dimensions are not equal (not a square matrix)')
        #     else:
        #         #  The determinant is a scalar value equal to the product of the main diagonal elements 
        #         # minus the product of it’s counter-diagonal elements.

        #         total = 0
        #         # Section 1: store indices in list for row referencing
        #         indices = list( range(self._rows) )
                    
        #         # Section 2: when at 2x2 submatrices recursive calls end
        #         if self._rows == 2 and self._columns == 2:
        #             val = self._matrix[0][0] * self._matrix[1][1] - self._matrix[1][0] * self._matrix[0][1]
        #             return val

        #         # Section 3: define submatrix for focus column and 
        #         #      call this function
        #         for fc in indices: # A) for each focus column, ...
        #             # find the submatrix ...
        #             # As = Matrix( list = [ [0.0] * self._columns for _ in range(self._rows) ] )

        #             As = self # B) make a copy, and ...
        #             As._matrix = As._matrix[1:] # ... C) remove the first row
        #             height = len(As._matrix) # D) 

        #             for i in range(height): 
        #                 # E) for each remaining row of submatrix ...
        #                 #     remove the focus column elements
        #                 As._matrix[i] = As._matrix[i][0:fc] + As._matrix[i][fc+1:] 

        #             sign = (-1) ** (fc % 2) # F) 
        #             # G) pass submatrix recursively
        #             sub_det = As.determinant()
        #             # H) total all returns from recursion
        #             total += sign * self._matrix[0][fc] * sub_det 

        #         return total



# Main code
def main():
    mat_a_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(mat_a_lst)

    mat_a = Matrix(list = mat_a_lst)
    print(mat_a)
    print(mat_a.trace)

    mat_b = Matrix(filename = r'C:\Users\Win10Pro\Downloads\ML_ACA\Python\Homework_Draft_6\input_matrix.txt')
    print(f"mat_b is: \n {mat_b}")

    mat_b.write_to_file(filename = r'C:\Users\Win10Pro\Downloads\ML_ACA\Python\Homework_Draft_6\output_matrix.txt')

    mat_c = mat_b.traspose()
    print(f"Transpose of mat_b: \n {mat_c}")

    mat_b.write_to_file(filename = r'C:\Users\Win10Pro\Downloads\ML_ACA\Python\Homework_Draft_6\transpose_matrix.txt')

    print(mat_b.shape)

    mat_d = mat_b + mat_c
    print(f"Adding mat_b abd mat_c: \n {mat_d}")

    mat_e = mat_a * mat_a.traspose()
    print(f"Pointwise multiplying mat_a and transpose of mat_a: \n {mat_e}")


    mat_f_lst = [[1, 2, 3], [4, 5, 6]]
    mat_f = Matrix(list = mat_f_lst)
    print(mat_f)

    mat_g_lst = [[7, 8, 0], [9, 10, 0], [11, 12, 0]]
    mat_g = Matrix(list = mat_g_lst)
    print(mat_g)
    print(f"Trace of mat_g: \n {mat_g.trace} \n")
    # print(mat_g.determinant)


    mat_h = mat_f @ mat_g
    print(f"Multiplying mat_g and mat_f: \n {mat_h}")



if __name__ == '__main__':
    main()
