def countConstructTabulation(target_string, word_bank):
    # number of characters in the target string
    m = len(target_string)
    # an array where dp[i] indicates the # of ways to generate
    # target_string[0:i] -- a.k.a target_string, characters from 0 to i-1 inclusive
    # using the words from the word bank
    # Assume there is 1 way we can generate the empty string at the beginning,
    # and there are 0 ways to generate every other prefix of target_string 
    # and continuously disprove it for some prefixes
    # dp[i] maps to target_string[0:i - 1] for each i in [0, m]
    dp = [0 for _ in range(m + 1)]
    # There is just 1 way to generate an empty string by taking no words
    # from the word_bank. This is the value we seed - our BASE CASE
    dp[0] = 1
    # go over each character in target_string
    for i, num_ways in enumerate(dp):
        # only consider substrings we can generate, because we cannot build further
        # combinations on top of those that can't be generated
        if num_ways > 0:
            # go over each word in the word_bank
            for word in word_bank:
                # check that it is a prefix at the position in consideration
                # in target_string, and it is non-empty to prevent infinite loops
                if isNonEmptyPrefixAt(what=word, of_what=target_string, starting_at=i):
                    # prefix length
                    prefix_len = len(word)
                    # where to propagate the current # of ways value
                    next_index = i + prefix_len
                    # actually propagate the current # of ways value
                    dp[next_index] += num_ways
    # return our actual answer, conveniently stored at the index == len(target_string)
    return dp[m]


def isNonEmptyPrefixAt(what, of_what, starting_at):
    prefix_len = len(what)
    # check that prefix is not empty to prevent infinite loops
    return prefix_len > 0 and of_what.find(what, starting_at) == starting_at


# Testing
print(countConstructTabulation("purple", ["purp", 'p', "ur", "le", "purpl"]))
print(countConstructTabulation("abcdef", ["ab", "abc", "cd", "def", "abcd", ""])) # true
print(countConstructTabulation("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # false
print(countConstructTabulation("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # true
print(countConstructTabulation("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", \
    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # false
