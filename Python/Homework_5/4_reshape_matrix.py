def solution_1(mat, r, c):
    # Number of elements in the initial matrix
    n = len(mat) * len(mat[0]) 

    if (r * c) != n:
        #Check if the reshaped matrix have the same size as initial, return initial otherwise.
        return mat
    
    #Initialize reshaped matrix
    reshaped_mat = [([None] * c) for _ in range(r)]
    
    cur_pos = 0 # Will be used to calculate position in reshaped matrix
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            reshaped_mat[cur_pos // c][cur_pos % c] = mat[i][j]
            cur_pos += 1
    return reshaped_mat


def solution_2(mat, r, c):
    if len(mat) * len(mat[0]) != r * c:
        return mat

    reshaped_mat = [[0 for _ in range(c)] for _ in range(r)]

    nums = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            nums.append(mat[i][j])

    k = 0
    for i in range(r):
        for j in range(c):
            reshaped_mat[i][j] = nums[k]
            k += 1

    return reshaped_mat


def solution_3(mat, r, c):
    if len(mat) * len(mat[0]) != r * c:
        return mat
    
    reshaped_mat = [[0 for _ in range(c)] for _ in range(r)]
    
    row, col = 0, 0
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            reshaped_mat[row][col] = mat[i][j]
            col += 1
            
            if col == c:
                col = 0
                row += 1
                
    return reshaped_mat



if __name__ == '__main__':

    # mat = [[1,2], [3,4]]; r = 1; c = 4
    mat = [[1,2], [3,4]]; r = 2; c = 4

    print(solution_1(mat, r, c))
    # print(solution_2(mat, r, c))
