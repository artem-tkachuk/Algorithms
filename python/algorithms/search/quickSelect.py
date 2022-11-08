# Quickselect using the original Hoare partitioning scheme
def quickselect(array, k):
    start, end = 0, len(array)

    assert end >= 1 and 0 < k <= end, "Incorrect arguments"

    while True:
        # arbitrary choice
        pivot = array[start]
        left, right = start + 1, end - 1
        # partially sort the array
        while left <= right:
            if array[left] > pivot and array[right] < pivot:
                swap(array, left, right)
            if array[left] <= pivot:
                left += 1
            if array[right] >= pivot:
                right -= 1
        # put the pivot in the correct position
        swap(array, start, right)
        # determine how to proceed
        if right == k - 1:
            return array[right]
        elif right > k - 1:
            end = right
        else:  # right < k - 1
            start = left


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def main():
    array = [1, 3, 71, 123, 124, 156, 814, 1294, 10024, 110000, 985181, 55516151]
    k = 12

    print(quickselect(array, k))

main()
