def countConstructMemoized(target_string, word_bank):
    return countConstructMemoizedHelper(target_string, word_bank, memo={})

def countConstructMemoizedHelper(target_string, word_bank, memo={}):
    # have we solved/cached this problem instance before
    if target_string in memo:
        return memo[target_string]
    # if we arrived at an empty string, and thus constructed a valid decomposition
    if target_string == "":
        return 1
    # otherwise initialize an empty counter to accumulate the answer
    count = 0
    # go through all the words from the bank
    for word in word_bank:
        # only branch out for the ones that are prefixes to the target_string
        if isNonEmptyPrefix(what=word, of_what=target_string):
            # length of the prefix we should cut out from the original target_string
            prefix_len = len(word)
            # whatever remains after slicing out the prefix
            suffix = target_string[prefix_len:]
            # branch out for the new target string
            count += countConstructMemoizedHelper(suffix, word_bank, memo)
                
    # cache out the # ways to construct the target_string
    memo[target_string] = count
    # return it to the parent/caller
    return count

def isNonEmptyPrefix(what, of_what):
    prefix_len = len(what)
    # check that it's the prefix which is not empty to prevent infinite loops
    return prefix_len > 0 and of_what.find(what) == 0

# Testing
print(countConstructMemoized("purple", ["purp", "p", "ur", "le", "purpl"]))
print(countConstructMemoized("abcdef", ["ab", "abc", "cd", "def", "abcd", ""])) # true
print(countConstructMemoized("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # false
print(countConstructMemoized("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # true
print(countConstructMemoized("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", \
    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # false
