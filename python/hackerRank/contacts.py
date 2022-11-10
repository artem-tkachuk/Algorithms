#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'contacts' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts 2D_STRING_ARRAY queries as parameter.
#

# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class PrefixTrie:
    def __init__(self):
        self.root = {"counter": 0}
        self.endSymbol = "*"

    # O(N) time | O(N) space
    def add(self, string: str):
        # total # of characters in the string
        n = len(string)
        # current node we are at -- set it to root at the start of inserting new suffix
        curr_node = self.root
        # go through each character of a particular suffic
        for i in range(n):
            curr_ch = string[i]
            # insert the character if not yet present
            if curr_ch not in curr_node:
                curr_node[curr_ch] = {"counter": 0}
            # Update the counter for the # of words that start with this character
            curr_node["counter"] += 1
            # move to the subsequent node to store subsequent character(s)
            curr_node = curr_node[curr_ch]
        # increment counter of the last node
        curr_node["counter"] += 1
        # Mark the end of the suffix, set the value of '*' to be True
        curr_node[self.endSymbol] = True
        
    # O(M) time | O(1) space
    def find(self, string: str):
        # TODO update
        # current node we are at
        curr = self.root
        # go through each character of the string in consideration
        for ch in string:
            if ch not in curr:
                # no matching contacts
                return 0
            else:
                curr = curr[ch]
        # if we didn't return a zero at this point, at least one contact exists with such a prefix ==> count all of them
    
        return curr["counter"]

def contacts(queries):
    # Store all the inserted strings in a Trie data structure
    trie = PrefixTrie()
    # array of output counters
    outputs = []
    # execute each query to the system
    for query in queries:
        # get operation type and it's argument
        [operation_type, argument] = query
        # it is an ADD
        if operation_type == 'add':
            trie.add(argument)
        else: # operation_type == 'find':
            num_contacts_with_prefix = trie.find(argument)
            outputs.append(num_contacts_with_prefix)

    return outputs

# Local testing
trie = PrefixTrie()
trie.add('art')
trie.add('ana')
trie.add('jack')
print(trie.find('a'))

# trie.add('s')
# trie.add('ss')
# trie.add('sss')
# trie.add('ssss')
# trie.add('sssss')
# print(trie.find('s'))
# print(trie.find('ss'))
# print(trie.find('sss'))
# print(trie.find('ssss'))
# print(trie.find('sssss'))
# print(trie.find('ssssss'))




#HackerRank code
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     queries_rows = int(input().strip())

#     queries = []

#     for _ in range(queries_rows):
#         queries.append(input().rstrip().split())

#     result = contacts(queries)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
