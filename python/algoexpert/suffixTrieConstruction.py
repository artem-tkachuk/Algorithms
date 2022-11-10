# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.
class SuffixTrie:
    def __init__(self, string: str):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # O(N^2) time | O(N^2) space
    def populateSuffixTrieFrom(self, string: str):
        # Suffixes of "babc": ["babc", "abc", "bc", "c"]
        # total # of characters in the string
        n = len(string)
        # go through each suffix 
        for i in range(n):
            self.insertSuffixStartingAt(i, string)
    
    # O(N) time | O(N) space
    def insertSuffixStartingAt(self, i: int, string: str):
        # total # of characters in the string
        n = len(string)
        # current node we are at -- set it to root at the start of inserting new suffix
        curr_node = self.root
        # go through each character of a particular suffic
        for j in range(i, n):
            curr_ch = string[j]
            # insert the character if not yet present
            if curr_ch not in curr_node:
                curr_node[curr_ch] = {}
            # move to the subsequent node to store subsequent character(s)
            curr_node = curr_node[curr_ch]
        # Mark the end of the suffix, set the value of '*' to be True
        curr_node[self.endSymbol] = True
        
    # O(M) time | O(1) space
    def contains(self, string: str):
        # current node we are at
        curr = self.root
        # go through each character of the string in consideration
        for ch in string:
            if ch not in curr:
                return False
            else:
                curr = curr[ch]
        # check that this is the actual suffix
        return self.endSymbol in curr


print(SuffixTrie("babc").contains("abc"))