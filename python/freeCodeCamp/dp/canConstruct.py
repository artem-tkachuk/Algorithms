def canConstructMemoized(target_string, word_bank):
    return canConstructMemoizedHelper(target_string, word_bank, memo={})

def canConstructMemoizedHelper(target_string, word_bank, memo={}):
    # have we solved/cached this problem instance before
    if target_string in memo:
        return memo[target_string]
    # if we arrived at an empty string, and thus constructed a valid decomposition
    if target_string == "":
        return True
    # go through all the words from the bank
    for word in word_bank:
        # only branch out for the ones that are prefixes to the target_string
        if isNonEmptyPrefix(what=word, of_what=target_string):
            # length of the prefix we should cut out from the original target_string
            prefix_len = len(word)
            # whatever remains after slicing
            suffix = target_string[prefix_len:]
            # branch out for the new target string
            if canConstructMemoizedHelper(suffix, word_bank, memo):
                # and potentially terminate early
                memo[target_string] = True
                return True
    # none of the prefixes worked
    memo[target_string] = False
    return False

def isNonEmptyPrefix(what, of_what):
    prefix_len = len(what)
    # check that prefix is not empty to prevent infinite loops
    return prefix_len > 0 and of_what.find(what) == 0

# Testing
print(canConstructMemoized("abcdef", ["ab", "abc", "cd", "def", "abcd", ""])) # true
print(canConstructMemoized("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # false
print(canConstructMemoized("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # true
print(canConstructMemoized("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", \
    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # false
