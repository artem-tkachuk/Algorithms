def allConstruct(target_string, word_bank):
    return allConstructHelper(target_string, word_bank, memo={})

def allConstructHelper(target_string, word_bank, memo={}):
    # have we already solved & cached this problem instance?
    # if so, retrieve it
    if target_string in memo:
        return memo[target_string]
    # empty string - affirmative base case
    if target_string == "":
        # there is 1 way to construct an empty string using words from word_bank
        # and it is to take 0 copies of each word from the word bank
        return [[]]
    # otherwise initialize an array that will hold all the ways it is possible 
    # to construct target_string from the words in the word_bank
    ways_to_construct_target = []
    # go through each word in the word bank
    for word in word_bank:
        # check that it is a VALID prefix
        if isNonEmptyPrefix(word, target_string):
            # get prefix length
            prefix_len = len(word)
            # get what remains after slicing out the prefix
            suffix = target_string[prefix_len:]
            # get all the ways to construct this suffix using words from the word bank
            # do a deep copy to prevent messing up the memoized arrays
            suffix_ways = allConstructHelper(suffix, word_bank, memo)
            # go through each way
            for way in suffix_ways: 
                # prepend the word(prefix) to each way to construct suffix
                # to obtain all ways to construct target_string
                way_with_prefix = [word, *way]
                # add a combination to the list of all ways to construct target_string
                ways_to_construct_target.append(way_with_prefix)
    # memoize all the ways we were able to find through recursion - can be empty list
    memo[target_string] = ways_to_construct_target
    # return it
    return ways_to_construct_target


def isNonEmptyPrefix(what, of_what):
    # prevent infinite loops by checking that prefix is non-empty
    return (len(what) > 0) and (of_what.find(what) == 0)


# Testing
print(allConstruct("purple", ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct("abcdef", ['ab', 'abc', 'cd', 'def', 'abcd', "ef", 'c']))
print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))
print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaz", ['a', "aa", "aaa", "aaaa", "aaaaa"]))