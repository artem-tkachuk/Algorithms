from typing import List

def knapsackWeightOnly(weights: List[int]) -> List[int]:
    # return list(knapsackWeightOnly_TopDown_Helper(weights, valuesSet=set()))
    return knapsackWeightOnly_BottomUp_Tabulation_Helper(weights)

# Top down solution, no memoization, bad time complexity 
def knapsackWeightOnly_TopDown_Helper(weights: List[int], valuesSet: set) -> List[int]:
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
        valuesSet |= knapsackWeightOnly_TopDown_Helper(weights_without_i, valuesSet)
    # return all possible sums for the current weights array
    return valuesSet
    

# bottom-up tabulation solution
def knapsackWeightOnly_BottomUp_Tabulation_Helper(weights: List[int]):
    



# Testing
print(knapsackWeightOnly([1, 3, 3, 5]))
print(knapsackWeightOnly([1, 2, 3]))


