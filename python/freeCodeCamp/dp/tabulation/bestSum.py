def bestSumTabulation(target, numbers):
    # an array that will eventually have answers for bestSum problem
    # for values in [0, target]
    dp = [None for _ in range(target + 1)]
    # Seed value, base case: it is always possible to generate a target of 0
    # by taking no numbers from the numbers array
    dp[0] = []
    # go through every element in dp
    for i, arr in enumerate(dp):
        # it is useless to propagate the False values
        if arr is not None:
            # go through each number in the numbers array
            for num in numbers:
                # compute the next index
                next_index = i + num
                # don't overshoot past the right end of the array
                if next_index <= target:
                    # a combination that sums to next_index
                    new_arr = [*arr, num]
                    # new and old lengths
                    new_len = len(new_arr)
                    # if dp[next_index] is None, set it's length to +\infty so that anything
                    # is less than this value
                    old_len = float('inf') if dp[next_index] is None else len(dp[next_index])
                    # only update if shorter
                    if new_len < old_len:
                        # propagate the current values to every value
                        # obtainable by adding elements of the numbers array 
                        # to the current value + append the number through which
                        # we got there in the first place
                        dp[next_index] = new_arr
    # return our actual answer
    return dp[target]

# Testing
print(bestSumTabulation(7, [5, 3, 4, 7]))
print(bestSumTabulation(8, [2, 3, 5]))
print(bestSumTabulation(8, [1, 4, 5]))
print(bestSumTabulation(100, [1, 25, 5, 2]))

