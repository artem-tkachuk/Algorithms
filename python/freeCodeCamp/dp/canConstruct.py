def canConstruct(target_string, word_bank):
    # if we arrived at an empty string, and thus constructed a valid decomposition
    if target_string == "":
        return True
    # else try all words from the word bank
    # # start off by saying it is not possible and potentially changing that to True
    # possible_to_construct = False
    # go through all the words from the bank
    for word in word_bank:
        # only branch out for the ones that are prefixes to the target_string
        if isPrefix(what=word, of_what=target_string):
            # length of the prefix we should cut out from the original target_string
            prefix_len = len(word)
            # whatever remains after slicing
            new_target_string = target_string[prefix_len:]
            # branch out for the new target string
            if canConstruct(new_target_string, word_bank):
                # and potentially terminate early
                return True
    # none of the prefixes worked
    return False

def isPrefix(what, of_what):
    prefix_len = len(what)
    target_string_len = len(of_what)
    # check that prefix is not empty and is at most as long as target 
    # to prevent infinite loops and incorrect slicing attempts
    return (0 < prefix_len <= target_string_len) and of_what.find(what) == 0

# Testing
print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", ""])) # true
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # false
print(canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])) # true
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", \
    ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])) # false
