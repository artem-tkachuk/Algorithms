class TrieNode():
    def __init__(self) -> None:
        self.children = {}
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        # self.root = {}
        # self.endSymbol = "*"
    
    # O(M) time | O(M) space, where M is he length of the word we insert
    def insert(self, word: str) -> None:
        # current node we are at -- set it to root at the start of inserting new suffix
        curr_node = self.root
        # go through each character of a particular suffic
        for curr_ch in word:
            # insert the character if not yet present
            if curr_ch not in curr_node.children:
                curr_node.children[curr_ch] = TrieNode()
            # move to the subsequent node to store subsequent character(s)
            curr_node = curr_node.children[curr_ch]
        # Mark the end of the suffix, set the value of '*' to be True
        curr_node.isEnd = True
        
    # O(M) time | O(1) space, where M is the length of the string we are searching for
    def search(self, word: str) -> bool:
        # current node we are at
        curr = self.root
        # go through each character of the string in consideration
        for ch in word:
            if ch not in curr.children:
                return False
            else:
                curr = curr.children[ch]
        # check that this is the actual suffix
        return curr.isEnd
        
    # O(M) time | O(1) space, where M is the length of the string we are searching for
    def startsWith(self, prefix: str) -> bool:
        # current node we are at
        curr = self.root
        # go through each character of the string in consideration
        for ch in prefix:
            if ch not in curr.children:
                return False
            else:
                curr = curr.children[ch]
        # check that this is the actual suffix
        return True


# Your Trie object will be instantiated and called as such:
trie = Trie()
word, prefix = '', ''
trie.insert(word)
print(trie.search(word))
print(trie.startsWith(prefix))