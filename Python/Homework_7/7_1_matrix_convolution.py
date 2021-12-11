# The result of convolution is a square matrix of (n-m+1) size:
# m < n
# n in the input square matrix size
# m is the kernel matrix size
#

from matrix import Matrix

def convolution_sliding(matrix, kernel):
    """
     Check if the matrix is square, find the convolution of 2 matrices:
    sliding-window multipliction of kernel matrix on input matrix
    """
    
    # Check if the self object is of type Matrix
    if isinstance (matrix, Matrix) and isinstance (kernel, Matrix):
        # Check the dimensions
        if matrix._columns == matrix._rows and kernel._columns == kernel._rows:
            # Create a new/3rd empty matrix of size (n-m+1)
            mat_conv_size = (matrix._rows - kernel._rows) + 1
            mat_conv = Matrix( list = [ ([0] * mat_conv_size) for _ in range(mat_conv_size) ] )
            
            # Sliding-window multipliction of kernel matrix on input matrix
            for i in range(mat_conv_size):
                for j in range(mat_conv_size):
                    curr_prod_sum = 0
                    for k in range(kernel._rows):
                        for l in range(kernel._columns):
                            curr_prod_sum += matrix._matrix[i+k][j+l] * kernel._matrix[k][l]
                    mat_conv._matrix[i][j] = curr_prod_sum
            
            return mat_conv
        else:
            raise ValueError('Got incorrect matrices: dimensions are not equal (not a square matrix)')
        

def main():
    matrix_in_lst = [[0, 1, 1, 1, 0, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 1, 1, 1, 0], \
                [0, 0, 0, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0, 0]]
    kernel_in_lst = [[1, 0, 1], [0, 1, 0], [1, 0, 1]]
    
    matrix_in = Matrix(list = matrix_in_lst)
    kernel_in = Matrix(list = kernel_in_lst)
    
    print( convolution_sliding(matrix_in, kernel_in) )
 
    
if __name__ == "__main__":
    main()
    