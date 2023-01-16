def funcHopSkipJump(matrix):
    N, M = len(matrix), len(matrix[0])

    if N > 2:
        return funcHopSkipJump(matrix[1:N - 1][1:M - 1])

    if N == 1:
        return matrix[0][0]