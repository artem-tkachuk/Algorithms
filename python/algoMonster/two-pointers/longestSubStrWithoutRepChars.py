# O(n^3) time, O(n) space
def brute_force(s: str) -> int:
    n = len(s)
    longest = 0

    # Start from every character in the string
    for start in range(n):
        for end in range(start, n + 1):
            sub_str = s[start:end]
            if len(sub_str) == len(set(sub_str)):
                longest = max(longest, len(sub_str))

    return longest

# O(n) time, O(n) space
from collections import defaultdict

def optimal(s: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(s)
    counts = defaultdict(int)
    
    left = 0
    max_len = 0

    for right in range(n): # [0, n - 1]
        ch_at_right = s[right]
        counts[ch_at_right] += 1

        while counts[ch_at_right] > 1:
            ch_at_left = s[left]
            counts[ch_at_left] -= 1
            left += 1

        max_len = max(max_len, right - left + 1)

    return max_len
        
# O(n) time, O(n) space
def longest_substring_without_repeating_characters(s: str) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    left, right = 0, 0 
    max_len = 0
    chars_present = set()

    while right < len(s):
        # Reset variables for the new substring
        curr_len = right - left
        # Find either the end or the index of the next repeating character
        while right < len(s) and s[right] not in chars_present:
            chars_present.add(s[right])
            curr_len += 1
            right += 1
        # Update max_len if necessary
        max_len = max(max_len, curr_len)

        if right < len(s):
            # left <= right
            # Guaranteed to have a character that is repeating
            # Move left pointer to the index of the next repeating character
            while s[left] != s[right]:
                if s[left] in chars_present:
                    chars_present.remove(s[left])
                left += 1
            chars_present.remove(s[left])    
            left += 1
    
    return max_len
        
    

s = "aaaaaaabaaa"
print(longest_substring_without_repeating_characters(s))
print(brute_force(s))
print(optimal(s))

s = "abccabcabcc"
print(longest_substring_without_repeating_characters(s))
print(brute_force(s))
print(optimal(s))

s = "aba"
print(longest_substring_without_repeating_characters(s))
print(brute_force(s))
print(optimal(s))

