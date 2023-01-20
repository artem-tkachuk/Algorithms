def canConstructTabulation(target_string, word_bank):
    m = len(target_string)
    dp = [False for _ in range(m + 1)]
    dp[0] = True

    for i, can_generate in enumerate(dp):
        if can_generate:
            for word in word_bank:
                if isNonEmptyPrefixAt(what=word, of_what=target_string, starting_at=i):
                    prefix_len = len(word)
                    next_index = i + prefix_len
                    dp[next_index] = True

    return dp[m]


def isNonEmptyPrefixAt(what, of_what, starting_at):
    prefix_len = len(what)
    # check that prefix is not empty to prevent infinite loops
    return prefix_len > 0 and of_what[starting_at:].find(what) == 0

# Testing
print(canConstructTabulation("abcdef", ["ab", "abc", "cd", "def", "abcd", ""])) # true
print(canConstructTabulation("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # false
print(canConstructTabulation("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # true
print(canConstructTabulation("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", \
    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # false
