def canSum(target, numbers):
    minNumber = min(numbers)
    return canSumHelper(target, numbers, minNumber)

def canSumHelper(target, numbers, minNumber, memo={}):
    if target == 0:
        return True

    if target < 0:
        return False

    # optimization - don't go through each element of a
    # potentially huge array when all of the branches are
    # guaranteed to not be taken
    if target - minNumber < 0:
        return False

    if target in memo:
        return memo[target]

    for num in numbers:
        if num != 0: 
            newTarget = target - num

            if canSumHelper(newTarget, numbers, minNumber, memo):
                memo[target] = True
                return True
    
    memo[target] = False
    
    return False

print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 6, 0]))
print(canSum(8, [2, 3, 5]))
print(canSum(300, [7, 14]))