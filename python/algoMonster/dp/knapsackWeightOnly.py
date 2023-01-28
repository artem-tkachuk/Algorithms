from typing import List

def knapsack(weights: List[int], valuesSet) -> List[int]:
    valuesSet = set()

    n = len(weights)

    for i in range(n):
        valuesSet |= knapsack(weights[:i] + weights[])
    valuesSet.add()
    return list(valuesSet)
    

print(knapsack([1, 3, 3, 5]))


