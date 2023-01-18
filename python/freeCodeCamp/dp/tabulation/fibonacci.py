def fibonacciTabulation(n):
    if n <= 0:
        return 0
    # a table to hold all fibonaccis computed so far
    fibTable = [0 for _ in range(n + 1)]
    # 1st Fibonacci number is 1
    fibTable[1] = 1

    for i in range(2, n + 1):
        fibTable[i] = fibTable[i - 1] + fibTable[i - 2]
    # elements of the fibTable correspond to those indicies' Fibonacci numbers 
    return fibTable[n]

def fibIteration(n):
    curr, prev = 1, 1
    
    for _ in range(n - 2):
        curr += prev
        prev = curr - prev

    return curr


print(f'Tests:')
print('Tabulation')
for i in range(1, 10):
    print(fibonacciTabulation(i))

print('Optimized')
for i in range(1, 10):
    print(fibIteration(i))