def solution_linear_search(a, k):
    L = 0
    possible = True
    
    while possible:
        # Test L + 1 and return L if not possible
        possible = False
        curr = 0
        
        for ribbon in a:
            curr += (ribbon // (L + 1))
            
            if curr >= k:
                L += 1
                possible = True
                break
                
    return L

def solution_binary_search(a, k):
    def possible(L):
        total = 0
        
        for ribbon in a:
            total += ribbon // L
            if total >= k:
                return True    
        
        return False
    
    left = 1 # min length of a ribbon
    right = max(a) # no ribbon can be cut into a piece larger than itself
    result = 0
    
    # binary search for various options for L instead of linear search of all possibilities
    # or sorting the array
    while left <= right:
        mid = (left + right) // 2
        
        if possible(mid):
            # update the maximum so far
            result = mid
            # and look for an even bigger value
            left = mid + 1
        else:
            # impossible to obtain the mid value
            # so look to the left
            right = mid - 1
    
    return result
    