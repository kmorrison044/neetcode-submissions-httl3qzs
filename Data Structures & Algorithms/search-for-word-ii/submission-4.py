class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLeaf = False

    def insert(self, word: str):
        curr = self

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        
        curr.isLeaf = True

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    
    def search(self, word: str):
        curr = self.root

        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return curr.isLeaf
    
    def prefSearch(self, pref: str):
        curr = self.root

        for c in pref:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        
        return True

class Solution:
    def __init__(self):
        self.trie = Trie()
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for w in words: self.root.insert(w)

        ROWS, COLS = len(board), len(board[0])
        res = set()
        curr = []
        def dfs(r: int, c: int, node: TrieNode):
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                board[r][c] == "#" or board[r][c] not in node.children):
                return

            ch = board[r][c]
            curr.append(ch)
            node = node.children[ch]
            if node.isLeaf:
                res.add("".join(curr))
            
            board[r][c] = "#"
            dfs(r + 1, c, node)
            dfs(r - 1, c, node)
            dfs(r, c + 1, node)
            dfs(r, c - 1, node)
            board[r][c] = ch
            curr.pop()

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, self.root)

        return list(res)