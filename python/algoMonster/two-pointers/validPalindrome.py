# O(n) space | O(1) time
def is_palindrome(s: str) -> bool:
    # WRITE YOUR BRILLIANT CODE HERE
    n = len(s)

    l, r = 0, n - 1

    while l < r:
        # find next alnum from left, if any
        if not s[l].isalnum():
            l += 1
            continue
        # find next alnum from right, if any
        if not s[r].isalnum():
            r -= 1
            continue
        # if the flow reached that line, both s[l] and s[r] are alnum chars
        # if both are alnum, but not equal, this is not a palindrome
        if s[l].lower() != s[r].lower():
            return False
        # At this point both s[l] and s[r] are alnum and equal
        # so update the pointers
        l += 1
        r -= 1

    # if all characters are checked, then it must be a palindrome
    return True 


# O(n) time | O(n) space
def is_palindrome_alternative(s: str) -> bool:
    listified_str = [ch.lower() for ch in s if ch.isalnum()]
    # length of the original string
    n = len(listified_str)
    # # listify a string to make it mutable
    # listified_str = list(s)
    # # move all alpha-numeric characters to the beginning of the listified string
    # slow = 0

    # for fast in range(n):
    #     if listified_str[fast].isalnum():
    #         # convert everything to lower right away
    #         listified_str[slow] = listified_str[fast].lower()
    #         slow += 1
    # # update the length
    # n = slow
    # check that it is a palindrome
    l, r = 0, n - 1

    while l < r:
        # if at least one character doesn't match, this is not palindrome
        if listified_str[l] != listified_str[r]:
            return False
        l += 1
        r -= 1

    return True

    print(s)


if __name__ == '__main__':
    s = " Do geese see ??God?"
    res = is_palindrome_alternative(s)
    print('true' if res else 'false')
