from typing import List

def knapsack(weights: List[int]) -> List[int]:
    return knapsackHelper(weights, valuesSet=set())

def knapsackHelper(weights: List[int], valuesSet: set = set()) -> List[int]:
    n = len(weights)

    if n == 0:
        return [0]

    for i in range(n):
        valuesSet |= set(knapsackHelper(weights[:i] + weights[(i + 1):], valuesSet))
    valuesSet.add(sum(weights))

    return list(valuesSet)
    

print(knapsack([1, 3, 3, 5]))
print(knapsack([1, 2, 3]))


