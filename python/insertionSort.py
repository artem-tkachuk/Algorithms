def insertionSort(arr):
    """
        Increasing order of elements
        An array of one element is trivially sorted ==> start with 2
        loop invariant: arr[0:i-1] is already sorted
    """
    for i in range(1, len(arr)):
        j = i
        # Until the the i'th element is not in the right place
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j] # Swap with the previous
            j -= 1
    return arr

# Testing
arr = [1, 2, 3, 4, 3, -2, 6, 4]
print(f'Original array: {arr}')
sorted_arr = insertionSort(arr)
print(f'Sorted array: {sorted_arr}')