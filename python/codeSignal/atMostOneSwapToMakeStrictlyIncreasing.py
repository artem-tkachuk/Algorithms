# Time complexity: O(m^2 * n^2 + m^3 * n) = O(m^2 * n^2)
# Space complexity: O(m)
def solution(numbers):
    if is_strictly_inc(numbers):
        return True
    else:
        for (i, num) in enumerate(numbers):
            # save original number at curr index
            original_num = num
            # stringify original number to enable easy digit swap
            str_original_num = str(original_num)
            n = len(str_original_num)
            
            # go over all possible swaps
            for j in range(n):
                for k in range(j + 1, n):
                    # swap the digits at j and k
                    curr_swap = swap_chars(str_original_num, j, k)
                    # set the current number to the current swap option
                    numbers[i] = int(curr_swap)
                    # check whether strictly increasing
                    if is_strictly_inc(numbers):
                        return True
                        
            # restore original number
            numbers[i] = original_num
            
        return False
    
def swap_chars(string, i, j):
    # convert to a list to enable easy swap
    c = list(string)
    c[i], c[j] = c[j], c[i]
    # join back to a string to convert to an int later
    return ''.join(c)
    
def is_strictly_inc(numbers):
    for i in range(1, len(numbers)):
        if numbers[i - 1] >= numbers[i]:
            return False
        
    return True
        
