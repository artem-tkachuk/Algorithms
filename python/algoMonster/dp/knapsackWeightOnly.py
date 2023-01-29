from typing import List

def knapsack(weights: List[int]) -> List[int]:
    return list(knapsackHelper(weights, valuesSet=set()))

def knapsackHelper(weights: List[int], valuesSet: set) -> List[int]:
    # number of elements in the weights array
    n = len(weights)
    # Base case: 0 elements in weights gives sum of 0
    if n == 0:
        return set([0])
    # Add the sum of weights itself to the set
    valuesSet.add(sum(weights))
    # go over each element and use it, recursively calling knapsack on remaining elements
    for i in range(n):
        weights_without_i = weights[:i] + weights[(i + 1):]
        # merge all possible sums of the weights array exclusing i'th elem to all the valuesSet
        valuesSet |= knapsackHelper(weights_without_i, valuesSet)
    # return all possible sums for the current weights array
    return valuesSet
    
# Testing
print(knapsack([1, 3, 3, 5]))
print(knapsack([1, 2, 3]))


