def gridTravelerTabulation(m, n):
    # create a 2D array/matrix of dimensions (m + 1) x (n + 1)
    # our final answer would be at matrix[m][n]
    # Array(m + 1).fill().map(() => Array(n + 1).fill(0)) in JavaScript
    matrix = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    # BASE CASE, in a 1x1 grid there is 1 way to get from top left to bottom right
    matrix[1][1] = 1
    # go through all rows
    for i in range(m + 1):
        # go through all columns
        for j in range(n + 1):
            # get our current elements
            current = matrix[i][j]
            # check the bounds
            if j + 1 <= n:
            # propagate the current to the right
                matrix[i][j + 1] += current
            # check the bounds
            if i + 1 <= m:
            # propagate the current to the bottom
                matrix[i + 1][j] += current
    
    # return final answer
    return matrix[m][n]

print(gridTravelerTabulation(1, 1))
print(gridTravelerTabulation(2, 3))
print(gridTravelerTabulation(3, 2))
print(gridTravelerTabulation(3, 3))
print(gridTravelerTabulation(18, 18))