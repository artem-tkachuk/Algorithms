from typing import List

def remove_duplicates(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(arr)

    slow = 0

    for fast in range(1, n):  # [1, n - 1]
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]

    return slow + 1



    # SOLUTION 2 using a while loop
    # slow, fast = 0, 0
    
    # while fast < n:
    #     if arr[fast] == arr[slow]:
    #         fast += 1
    #     else:
    #         slow += 1
    #         arr[slow] = arr[fast]
            
    # return slow + 1

if __name__ == '__main__':
    arr = [0, 0, 1, 1, 1, 2, 2, 3]
    res = remove_duplicates(arr)
    print(' '.join(map(str, arr[:res])))
