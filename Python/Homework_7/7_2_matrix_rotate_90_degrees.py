# matrix[:] = [[matrix[i][j] for i in range(n-1,-1,-1)] for j in range(n)]

from matrix import Matrix

def matrix_rotate_90(matrix):
    """
     Check if the matrix is square (n x n) and return it but rotated by 90 degrees:
    value manipulation is done in-palce.
    """
    
    # Check if the self object is of type Matrix
    if isinstance (matrix, Matrix):
        # Check the dimensions
        if matrix._columns == matrix._rows:
            # Rotate the matrix by 90 degrees: 
            # 1.) Matrix transpose
            for i in range(matrix._columns):
                for j in range(i, matrix._rows):
                    # swap values
                    matrix._matrix[i][j], matrix._matrix[j][i] = matrix._matrix[j][i], matrix._matrix[i][j]
            
            # 2.) Reverse the elements in each row i.e. mirror-reflecting the matrix.
            for i in range(matrix._columns):
                for j in range((matrix._rows // 2)):  # Half of the elements, except the middle element.
                    # swap values
                    matrix._matrix[i][j], matrix._matrix[i][-j-1] = matrix._matrix[i][-j-1], matrix._matrix[i][j]
                    
            return matrix
        else:
            raise ValueError('Got incorrect matrix: dimensions are not equal (not a square matrix)!')
    

def main():
    matrix_1_lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matrix_1 = Matrix(list = matrix_1_lst)
    print( matrix_rotate_90(matrix_1) )
 
    matrix_2_lst = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    matrix_2 = Matrix(list = matrix_2_lst)
    print( matrix_rotate_90(matrix_2) )
 
    
if __name__ == "__main__":
    main()