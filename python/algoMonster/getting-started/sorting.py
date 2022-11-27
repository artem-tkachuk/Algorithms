from typing import List

def swap(list: List[int], i, j):
    list[i], list[j] = list[j], list[i]

# O(n^2) time | O(1) space
def insertion_sort(arr: List[int]) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(arr)

    for i in range(1, n):
        curr_idx = i
        while curr_idx > 0 and arr[curr_idx] < arr[curr_idx - 1]:
            swap(arr, curr_idx, curr_idx - 1)
            curr_idx -= 1

    return arr

# O(n^2) time | O(1) space
def selection_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in range(n):
        # find the minimum in the unsorted pile
        min_idx = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # put the found minimum to the sorted pile
        swap(arr, i, min_idx)

    return arr

# O(n^2) time | O(1) space
def bubble_sort(arr: List[int]) -> List[int]:
    n = len(arr)

    for i in reversed(range(n)):  # [n - 1, n - 2, ..., 0]
        swapped = False

        for j in range(i):
            if arr[j] > arr[j + 1]:
                swap(arr, j, j + 1)
                swapped = True

        if not swapped:
            break

    return arr

# O(n\log(n)) time | O(n) space
def merge_sort(arr: List[int]) -> List[int]:
    # Length of the passed array
    n = len(arr)
    # empty list or one element -- sorted by definition
    if n <= 1:
        return arr
    else:
        # at this point n >= 2
        midpoint = n // 2
        # sort two sub arrays
        left_list = merge_sort(arr[:midpoint])
        right_list = merge_sort(arr[midpoint:])
        # Shortcut for their length
        len_left, len_right = len(left_list), len(right_list)
        # merge the two sorted sub arrays
        final_list = []
        # pointers to current elements in left and right subarrays
        l, r = 0, 0
        # continue adding while not every element is in final list
        while l < len_left or r < len_right:
            # Get the actual elements in consideration
            # at least one of those is not +\infty (which means out of bounds)
            curr_left = left_list[l] if l < len_left else float('inf')
            curr_right = right_list[r] if r < len_right else float('inf')
            # add smaller one
            if curr_left <= curr_right:
                final_list.append(curr_left)
                l += 1
            else:  # curr_right <= curr_left
                final_list.append(curr_right)
                r += 1
        # Return the final merged list
        return final_list

def merge_sort_with_helper(arr: List[int]) -> List[int]:
    # Helper function
    def merge_sort_helper(arr: List[int], start: int, end: int) -> List[int]:
        n = end - start
        # empty list or one element -- sorted by definition
        if n <= 1:
            return arr[start:end]
        else:
            # at this point n >= 2
            midpoint = n // 2
            # sort two sub arrays
            left_list = merge_sort_helper(arr, start, start + midpoint)
            right_list = merge_sort_helper(arr, start + midpoint, end)
            # Shortcut for their length
            len_left, len_right = len(left_list), len(right_list)
            # merge the two sorted sub arrays
            final_list = []
            # pointers to current elements in left and right subarrays
            l, r = 0, 0
            # continue adding while not every element is in final list
            while l < len_left or r < len_right:
                # Get the actual elements in consideration
                # at least one of those is not +\infty (which means out of bounds)
                curr_left = left_list[l] if l < len_left else float('inf')
                curr_right = right_list[r] if r < len_right else float('inf')
                # add smaller one
                if curr_left < curr_right:
                    final_list.append(curr_left)
                    l += 1
                else:  # curr_right <= curr_left
                    final_list.append(curr_right)
                    r += 1
            # Return the final merged list
            return final_list


    # Call the helper function on the whole array
    sorted_list = merge_sort_helper(arr, 0, len(arr))
    # return the final sorted list returned by the helper function
    return sorted_list

# O(...) time | O(...) space
def quickSort(arr: List[int]) -> List[int]:
    # TODO implement quicksort here
    pass

if __name__ == '__main__':
    unsorted_list = [7, 2, 6, 3, 4, 8, 12, 2, -3]

    # Insertion sort
    res = insertion_sort(unsorted_list)
    print(f'Sorted with insertion sort:')
    print(' '.join(map(str, res)))
    # Selection sort
    res = selection_sort(unsorted_list)
    print(f'Sorted with selection sort:')
    print(' '.join(map(str, res)))
    # Bubble sort
    res = bubble_sort(unsorted_list)
    print(f'Sorted with bubble sort:')
    print(' '.join(map(str, res)))
    # Merge sort
    res = merge_sort(unsorted_list)
    print(f'Sorted with merge sort:')
    print(' '.join(map(str, res)))
