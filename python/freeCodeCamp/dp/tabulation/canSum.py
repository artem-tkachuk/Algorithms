def canSumTabulation(target, numbers):
    # an array that will eventually have answers for canSum problem
    # for values in [0, target]
    dp = [False for _ in range(target + 1)]
    # Seed value, base case: it is always possible to generate a target of 0
    # by taking no numbers from the numbers array
    dp[0] = True
    # go through every element in dp
    for i, elem in enumerate(dp):
        # it is useless to propagate the False values
        if elem == True:
            # go through each number in the numbers array
            for num in numbers:
                # compute the next index
                next_index = i + num
                # don't overshoot past the right end of the array
                if next_index <= target:
                    # propagate the True value to every value
                    # obtainable by adding elements of the numbers array 
                    # to the current value
                    dp[next_index] = True
    # return our actual answer
    return dp[target]

# Testing
print(canSumTabulation(7, [2, 3]))
print(canSumTabulation(7, [5, 3, 4, 7]))
print(canSumTabulation(7, [2, 6]))
print(canSumTabulation(8, [2, 3, 5]))
print(canSumTabulation(300, [7, 14]))



