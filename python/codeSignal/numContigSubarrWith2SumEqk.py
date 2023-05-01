# Passes 6 / 10

# O((n - m) * m^2) time
# O(1) space

# def solution(a, m, k):
#     count = 0
#     n = len(a)
    
#     for i in range(n - m + 1):
#         found = False
        
#         for j in range(i, i + m - 1):
            
#             for r in range(j + 1, i + m):
                
#                 if a[j] + a[r] == k:
#                     count += 1
#                     found = True
#                     break
            
#             if found:
#                 break
                
#     return count


def solution(a, m, k):
    n = len(a)
    
    count = 0
    i = 0
    
    while i <= n - m:
        found = False
        
        nums_in_window = {
            a[i]: i
        }
        
        for j in range(i + 1, i + m):
                            
            complement = k - a[j]
                
            if complement in nums_in_window:
                bound = min(n - m, nums_in_window[complement])
                count += (bound - i + 1)
                i = bound + 1
                found = True
                break
            else:
                nums_in_window[a[j]] = j
                
        if not found:
            i += 1
                
    return count


a = [2, 4, 7, 5, 3, 5, 8, 5, 1, 7]
m = 4
k = 10

solution(a, m, k)