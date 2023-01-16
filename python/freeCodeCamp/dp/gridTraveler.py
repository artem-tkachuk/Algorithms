def gridTravelerNoMemo(m, n):
    # invalid grid, either of dimensions is 0
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        return gridTravelerNoMemo(m - 1, n) + gridTravelerNoMemo(m, n - 1)

# print(gridTravelerNoMemo(1, 1))
# print(gridTravelerNoMemo(2, 3))
# print(gridTravelerNoMemo(3, 2))
# print(gridTravelerNoMemo(3, 3))
# print(gridTravelerNoMemo(18, 18))

def gridTravelerMemo(m, n):
    return gridTravelerMemoHelper(m, n, dp={})

def gridTravelerMemoHelper(m, n, dp={}):
    if (n, m) in dp or (m, n) in dp:
        return dp[(n, m)] if (n, m) in dp else dp[(m, n)]
    
    if m == 0 or n == 0:
        return 0
    elif m == 1 and n == 1:
        return 1
    else:
        dp[(m, n)] = gridTravelerMemoHelper(m - 1, n, dp) + gridTravelerMemoHelper(m, n - 1, dp)
        
        return dp[(m, n)]

print(gridTravelerMemo(1, 1))
print(gridTravelerMemo(2, 3))
print(gridTravelerMemo(3, 2))
print(gridTravelerMemo(3, 3))
print(gridTravelerMemo(18, 18))