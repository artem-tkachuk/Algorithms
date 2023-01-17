def fibRecursive(n):
    if n <= 2:
        return 1
    else:
        return fibRecursive(n - 1) + fibRecursive(n - 2)

# memoization
# python dictionary
# keys will be arguments to function, values will be the return values
def fibMemoization(n):
    return fibMemoizationHelper(n, dp={})
    
def fibMemoizationHelper(n, dp={}):
    if n in dp:
        return dp[n]
    if n <= 2:
        return 1
    else:
        dp[n] = fibMemoizationHelper(n - 1, dp) + fibMemoizationHelper(n - 2, dp)
        return dp[n]

def fibIteration(n):
    if n <= 2:
        return 1
    else:
        curr, prev = 1, 1
        for _ in range(n - 2):
            curr += prev
            prev = curr - prev

        return curr

print(f'Memoization results:')
for i in range(1, 10):
    print(fibMemoization(i))


print(f'Iteration results:')
for i in range(1, 10):
    print(fibIteration(i))
