def matrixMultiplication(matrix1, matrix2):
    # Each matrix is a list of lists
    assert type(matrix1) == list and type(matrix1[0] == list)
    assert type(matrix2) == list and type(matrix2[0] == list)

    # Dimensions
    x, y = len(matrix1), len(matrix1[0])
    q, z = len(matrix2), len(matrix2[0])

    assert y == q, "Dimensions don't match ==> can't perform multiplication"

    C = [[0 for _ in range(z)] for _ in range(x)]

    for i in range(x):
        for j in range(z):
            for k in range(y):
                C[i][j] += matrix1[i][k] * matrix2[k][j]

    return C


# Testing
matrix1 = [
    [1, 1],
    [1, 1]
]

matrix2 = [
    [1, 1, 2],
    [1, 1, 2]
]

print(matrixMultiplication(matrix1, matrix2))