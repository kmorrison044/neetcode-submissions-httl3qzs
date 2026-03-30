public class TrieNode {
    public Dictionary<char, TrieNode> children = new Dictionary<char, TrieNode>();
    public bool isLeaf = false;

    public void insert(string word) {
        TrieNode curr = this;
        foreach (char c in word) {
            if (!curr.children.ContainsKey(c)) {
                curr.children[c] = new TrieNode();
            }
            curr = curr.children[c];
        }
        curr.isLeaf = true;
    }
}
public class Solution {
    public TrieNode root = new TrieNode();

    public List<string> FindWords(char[][] board, string[] words) {
        foreach (string w in words) {
            root.insert(w);
        }

        var ROWS = board.Length;
        var COLS = board[0].Length;
        var res = new List<string>();
        var curr = new List<char>();

        void backtrack(int r, int c, TrieNode node) {
            if (r < 0 || c < 0 || r >= ROWS || c >= COLS ||
            board[r][c] == '#' || !node.children.ContainsKey(board[r][c])) {
                return;
            }

            var ch = board[r][c];
            curr.Add(ch);
            node = node.children[ch];

            if (node.isLeaf) {
                res.Add(string.Join("", curr));
                node.isLeaf = false;
            }

            board[r][c] = '#';
            backtrack(r + 1, c, node);
            backtrack(r - 1, c, node);
            backtrack(r, c + 1, node);
            backtrack(r, c - 1, node);
            board[r][c] = ch;
            curr.RemoveAt(curr.Count - 1);
        }

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                backtrack(r, c, root);
            }
        }
        return res;
    }
}
