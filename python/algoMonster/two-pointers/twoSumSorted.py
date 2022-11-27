from typing import List

def two_sum_sorted(arr: List[int], target: int) -> List[int]:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(arr)
    l, r = 0, n - 1

    while True:
        curr_two_sum = arr[l] + arr[r]

        if curr_two_sum == target:
            return l, r
        elif curr_two_sum > target:
            r -= 1
        else:  # curr_two_sum < target:
            l += 1

if __name__ == '__main__':
    arr = [2, 3, 4, 5, 8, 11, 18]
    target = 8
    res = two_sum_sorted(arr, target)
    print(' '.join(map(str, res)))
