# Returns ALL the starting indices where pattern occurs in string
# Indices are from 0 to n - 1
def findMatch(string, pattern):
    occurrences = []

    n = len(string)
    m = len(pattern)

    for i in range(n - m + 1):  # [0, n - m + 1) = [0, n - m]
        j = 0
        while j < m and string[i + j] == pattern[j]:
            j += 1
        if j == m:
            occurrences.append(i)

    return occurrences


# Testing
string = "abaababbaba"
pattern = "abba"
print(findMatch(string, pattern))

