# O(n) time, O(1) space
def kadanesAlgorithm(array: list[int]):
    maxEndindHere = float('-inf')
    # Target return value: maximum sub of any subarray
    maxSoFar = float('-inf')

    for number in array:
        maxEndindHere = max(number, maxEndindHere + number)
        maxSoFar = max(maxEndindHere, maxSoFar)

    return maxSoFar

def printMaximumSumContiguousSubarray(array: list[int]):
    # Total # of elements in the array
    n = len(array)
    start, end = 0, 0  # start and end indices of the maximum sum contiguous subarray

    maxEndindHere = float('-inf')
    # Target return value: maximum sub of any subarray
    maxSoFar = float('-inf')

    for i in range(n):
        # get the actual number at the index
        number = array[i]
        # update maxEndingHere if needed
        if number > maxEndindHere + number:
            start = i
            maxEndindHere = number
        else:
            maxEndindHere += number
        
        if maxEndindHere > maxSoFar:
            maxSoFar = maxEndindHere
            end = i

    # Print the resulting array, space-separated
    for i in range(start, end + 1):
        print(array[i], end=' ')
    print(f"\nmax sum = {maxSoFar}")

printMaximumSumContiguousSubarray([-2, 5, 64, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 100])