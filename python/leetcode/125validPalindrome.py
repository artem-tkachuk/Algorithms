class Solution:
    # O(n) time | O(1) space
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1  # two pointers

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            # at this point both a[left] and a[right] are alnum
            if s[right].lower() != s[left].lower():
                return False
            else:
                left += 1
                right -= 1

        return True