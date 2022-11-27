from typing import List

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def move_zeros(nums: List[int]) -> None:
    # WRITE YOUR BRILLIANT CODE HERE
    # Length of the array in consideration
    n = len(nums)
    # start off from the start
    slow = 0
    # fast pointer travreses all the array
    # repeatedly finding the next non-zero element and swapping it
    # with zero pointed to by the slow pointer
    # or uselessly swaps with itself (but this makes code generalizable)
    for fast in range(n):
        # found non-zero element ==> move to earlier
        if nums[fast] != 0:
            # at this point slow points to 0 or they point to the same element
            swap(nums, slow, fast)
            slow += 1
    # return the final array
    return nums



    # # ALTERNATIVE SOLUTION
    # # i will end up at the position corresponding to the index of last non-zero element
    # i = 0
    # for number in nums:
    #     if number != 0:
    #         nums[i] = number
    #         i += 1
    # # fill the rest with 0
    # for j in range(i, len(nums)):
    #     nums[j] = 0

    # return nums


if __name__ == '__main__':
    nums = [int(x) for x in input().split()]
    move_zeros(nums)
    print(' '.join(map(str, nums)))
