def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix_ = []
        for j in range(m):
            matrix_.append(value)
        matrix.append(matrix_)
    return matrix


print(get_matrix(2, 2, 10))
print(get_matrix(3, 5, 42))
print(get_matrix(4, 2, 13))
