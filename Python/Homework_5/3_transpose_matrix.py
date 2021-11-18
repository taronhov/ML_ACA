# matrix = [[1,2,3], [4,5,6], [7,8,9]]
# matrix = [[1,2,3], [4,5,6]]

matrix_str = input("Enter matrix: ")
matrix_str = list(matrix_str.strip('\ []').replace(']', '').split('['))

matrix = []
for index, value in enumerate(matrix_str):
    matrix.append( list( map(int, value.strip('\ ,').split(',')) ) )

# print(matrix)

row = len(matrix)
col = len(matrix[0])


# 1st solution
# t_matrix = []
# temp_matrix =[]
# for i in range(col):
#     for j in range(row):
#         temp_matrix.append(matrix[j][i])
#         t_matrix.append(temp_matrix)
#         temp_matrix = []

# print(t_matrix)


# 2nd solution
t_matrix = []
for i in range(col):
    t_matrix.append([0 for _ in range(row)])

for i in range(col):
    for j in range(row):
        t_matrix[i][j] = matrix[j][i]

print(t_matrix)