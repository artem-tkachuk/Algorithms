def howSum(target, numbers):
    # invalid call
    if target < 0:
        return None
    # found a valid combination! ==> initiate the array collection
    if target == 0:
        return []
    # go through all children to see if some of the work out
    for num in numbers:
        newTarget = target - num
        # TODO change return value        
        validCombination = howSum(newTarget, numbers) 
        
        if validCombination is not None:
            # validCombination.append(num)
            return [*validCombination, num]
    # None of the children worked out
    return None

def howSumMemoized(target, numbers):
    return howSumMemoizedHelper(target, numbers, memo={})

def howSumMemoizedHelper(target, numbers, memo={}):
    # look the target sum up in cache
    if target in memo:
        return memo[target]
    # invalid call
    if target < 0:
        return None
    # found a valid combination! ==> initiate the array collection
    if target == 0:
        return []
    # otherwise go through all children to see if some of the work out
    for num in numbers:
        # prevent infinite loops
        if num != 0:
            newTarget = target - num
            # don't forget to pass down the memo object        
            valid_combination = howSumMemoizedHelper(newTarget, numbers, memo) 
            
            if valid_combination is not None:
                # validCombination.append(num)
                memo[target] = [*valid_combination, num]
                # return the (now computed and cached) value
                return memo[target]
    # None of the children worked out
    # cache
    memo[target] = None
    # and return
    return None

print(howSumMemoized(7, [2, 3]))
print(howSumMemoized(7, [5, 3, 4, 7]))
print(howSumMemoized(7, [2, 4]))
print(howSumMemoized(8, [2, 3, 5]))
print(howSumMemoized(300, [7, 0, 14]))



