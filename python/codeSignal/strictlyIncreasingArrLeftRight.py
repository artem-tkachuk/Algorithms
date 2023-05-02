def solution(a):
    # Solution 1
    # b = a[0]
    # left, right = 1, len(a) - 1
    
    # while left <= right:
    #     if b >= a[right] or a[right] >= a[left]:
    #         break
    #     else:
    #         b = a[left]
    #         left += 1
    #         right -= 1
    
    # if left > right:
    #     return True
    # elif left < right:
    #     return False
    # else:
    #     # case left == right
    #     return a[left] > b
    
    # Solution 2
    b = float('-inf')
    
    left, right = 0, len(a) - 1
    
    while left <= right:
        # Found non-strinctly-increasing pair of elements
        if a[left] <= b:
            return False
        else:
            # odd # of elements in original arr
            # and we already verified increasing for left, but a[left] == a[right]
            if left == right:
                return True
            else:
                # "Add" left pointer's element to new array
                b = a[left]
                # Found non-strinctly-increasing pair of elements
                if a[right] <= b:
                    return False
                else:
                    # "Add" right pointer's element to new array
                    b = a[right]
                    left += 1
                    right -= 1
                    
    return True