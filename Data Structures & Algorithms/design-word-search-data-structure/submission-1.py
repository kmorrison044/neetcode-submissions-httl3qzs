class TrieNode():
    def __init__(self):
        self.children = {}
        self.isLeaf = False
        
# This is basically a Trie
class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    # Classic insert function for PrefTrie
    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isLeaf = True

    # Search function changes here since dots can match
    # Any letter. Run dfs starting at the root and passing the current
    # index of the word. Loop over the word starting at the index
    # that was passed in, if the current char is a ".", then loop
    # over every character stored in the trie, and run dfs to see
    # if the remaining characters at that node match the rest of the word.
    # if so, return true, otherwise false. If the char is not ".", then
    # simply run the regular trie search algo.
    def search(self, word: str) -> bool:
        def dfs(i, root):
            curr = root
    
            for j in range(i, len(word)):
                c  = word[j]
                if c == ".":
                    for child in curr.children.values():
                        if dfs(j + 1, child):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr = curr.children[c]
    
            return curr.isLeaf

        return dfs(0, self.root)