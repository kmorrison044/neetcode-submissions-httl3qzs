# Create TrieNode class that contains children
# hashmap and isLeaf flag to determine if we have
# inserted this node before
class TrieNode():
    def __init__(self):
        self.children = {}
        self.isLeaf = False

class PrefixTree:
    def __init__(self):
        # Init the tree to a TrieNode()
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        # Set curr to root, iterate through the word and check
        # if the current char is is in the current TrieNode's children
        # hashmap. If not, then create a TrieNode in the current TrieNode's
        # children hashmap with the key of the character. Finally set
        # isLeaf to true after the loop to say we have inserted this word
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isLeaf = True

    def search(self, word: str) -> bool:
        # Set curr to root, then iterate over every character in the word.
        # if the character is not in the current TrieNode's children hashmap,
        # then return False (i.e the word hasn't been inserted). Otherwise,
        # continue updating curr to the next TrieNode. If it exits the for loop,
        # then check if the Node's isLeaf value is True, meaning we've inserted the
        # word in the past.
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return curr.isLeaf

    def startsWith(self, prefix: str) -> bool:
        # Set curr to root. Iterate over every character in the prefix and check
        # if the current character is in the current TrieNode's children hashmap,
        # if not then return False (there is no word in the tree with this prefix)
        # otherwise update curr to the next TrieNode. If it breaks from the for loop,
        # return True.
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True