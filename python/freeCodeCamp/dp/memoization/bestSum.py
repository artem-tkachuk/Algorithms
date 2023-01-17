from collections import defaultdict

# TODO: optimize so that it does not go if it has already found a valid combo of a shorter length


def bestSumMemoized(target, numbers):
    min_number = min(numbers)
    shortest_len = float('inf')
    return bestSumHelperMemoized(target, numbers, min_number, shortest_len, memo={})

def bestSumHelperMemoized(target, numbers, min_number, overall_shortest_len, memo={}):
    if overall_shortest_len < 0:
        return None
    # look the target sum up in cache
    if target in memo:
        return memo[target]
    # invalid call
    if target < 0:
        return None
    # found a valid combination! ==> initiate the array collection
    if target == 0:
        return []
    # terminate without checking anything
    if target < min_number:
        return None
    # otherwise look at how we can decompose the target sum
    # initialize the cache
    shortest_combination = None
    shortest_len = float('inf')
    # go through all children
    for num in numbers:
        # avoid infinite loops
        if num != 0:
            # compute the new target we are trying to decompose
            new_target = target - num
            # get the shortest decomposition of the new target
            new_target_combination = bestSumHelperMemoized(new_target, numbers, min_number, shortest_len - 1, memo)
            # check that it exists
            if new_target_combination is not None:
                # make a deep copy to make sure the recursion does not crash
                curr_combination = new_target_combination.copy()
                # add the edge weight to the combination so that sum(shortest_combination)
                curr_combination.append(num)
                # see if this combination is the shortest seen so far or not
                if len(curr_combination) < shortest_len:
                    # if it is - update the shortest to be the current
                    # do a deep copy to avoid collecting giant object!
                    shortest_combination = curr_combination
                    # update length
                    shortest_len = len(curr_combination)
    # cache the obtained result for this target
    memo[target] = shortest_combination
    # return the shortest found combination
    return shortest_combination

# Testing
print(bestSumMemoized(7, [5, 3, 4, 7]))
print(bestSumMemoized(8, [2, 3, 5]))
print(bestSumMemoized(8, [1, 4, 5]))
print(bestSumMemoized(100, [1, 2, 5, 25]))