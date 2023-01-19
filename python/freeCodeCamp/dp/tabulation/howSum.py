def howSumTabulation(target, numbers):
    # an array that will eventually have answers for howSum problem
    # for values in [0, target]
    dp = [None for _ in range(target + 1)]
    # Seed value, base case: it is always possible to generate a target of 0
    # by taking no numbers from the numbers array
    dp[0] = []
    # go through every element in dp
    for i, arr in enumerate(dp):
        # it is useless to propagate the None values
        if arr is not None:
            # go through each number in the numbers list
            for num in numbers:
                # compute the next index
                next_index = i + num
                # don't overshoot past the right end of the array
                if next_index <= target:
                    # propagate the current values to every value
                    # obtainable by adding elements of the numbers array 
                    # to the current value + append the number through which
                    # we got there in the first place
                    dp[next_index] = [*arr, num]
    # return our actual answer
    return dp[target]

# Testing
print(howSumTabulation(7, [2, 3]))
print(howSumTabulation(7, [5, 3, 4, 7]))
print(howSumTabulation(7, [2, 4]))
print(howSumTabulation(8, [2, 3, 5]))
print(howSumTabulation(300, [7, 14]))



