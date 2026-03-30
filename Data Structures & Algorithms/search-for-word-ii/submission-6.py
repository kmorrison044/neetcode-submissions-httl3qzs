# Create just the TrieNode with the insert func and not the whole Trie.
# Pass in the actual node in the backtracking algo,
# rather than searching the whole trie over and over.
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

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # Start by inserting every word in the Trie
        for w in words: self.root.insert(w)

        # Set needed vars
        ROWS, COLS = len(board), len(board[0])
        # Make sure it is a set to remove dups
        res = set()
        curr = []
        def backtrack(r: int, c: int, node: TrieNode):
            # Check if current r and c are in bounds, if the current char
            # has already been used, and if the current char in your trie's
            # children
            if (r < 0 or c < 0 or r >= ROWS or c >= COLS or
                board[r][c] == "#" or board[r][c] not in node.children):
                return

            # Grab the current char, append it to curr list of chars,
            # update node
            ch = board[r][c]
            curr.append(ch)
            node = node.children[ch]
            # if the word is in the trie, then add to result
            if node.isLeaf:
                res.add("".join(curr))
            
            # Select word, then backtrack
            board[r][c] = "#"
            backtrack(r + 1, c, node)
            backtrack(r - 1, c, node)
            backtrack(r, c + 1, node)
            backtrack(r, c - 1, node)
            # Deselect word and pop from curr
            board[r][c] = ch
            curr.pop()

        # Run the backtrack on each cell so that each cell
        # has a turn to be the "initial" cell run
        for r in range(ROWS):
            for c in range(COLS):
                backtrack(r, c, self.root)

        # Convert res back to list
        return list(res)