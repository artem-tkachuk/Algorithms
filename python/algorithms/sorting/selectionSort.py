def selectionSort(arr):
    """
        Increasing order of elements
        loop invariant: arr[0:i-1] is already sorted
    """
    n = len(arr)

    for i in range(n - 1):
        # Find index of the minimum element in the unsorted portion, namely [i + 1, n]
        minIdx = i
        for j in range(i + 1, n):
            if arr[j] < arr[minIdx]:
                minIdx = j
        # Swap i'th and minIdx'th element in arr
        swap(arr, minIdx, i)

    return arr


def swap(arr, i, j):
        arr[i], arr[j] = arr[j], arr[i]


# Testing
arr = [1, 2, 3, 4, 3, -2, 6, 4]
print(f'Original array: {arr}')
sorted_arr = selectionSort(arr)
print(f'Sorted array: {sorted_arr}')