class TrieNode {
    HashMap<Character, TrieNode> children = new HashMap<>();
    String word = null;

    public void insert(String word) {
        TrieNode curr = this;
        for (char c : word.toCharArray()) {
            curr.children.putIfAbsent(c, new TrieNode());
            curr = curr.children.get(c);
        }
        curr.word = word;
    }
}

class Solution {
    private Set<String> res;

    public List<String> findWords(char[][] board, String[] words) {
        TrieNode root = new TrieNode();

        for (String word : words) {
            root.insert(word);
        }

        int ROWS = board.length, COLS = board[0].length;
        res = new HashSet<>();

        for (int r = 0; r < ROWS; r++) {
            for (int c = 0; c < COLS; c++) {
                backtrack(board, r, c, root);
            }
        }

        return new ArrayList<>(res);
    }

    private void backtrack(char[][] board, int r, int c, TrieNode node) {
        int ROWS = board.length, COLS = board[0].length;

        if (r < 0 || c < 0 || r >= ROWS || c >= COLS ||
            board[r][c] == '#' || !node.children.containsKey(board[r][c])) {
                return;
            }

        char ch = board[r][c]; 
        node = node.children.get(ch);
        if (node.word != null) {
            res.add(node.word);
        }

        board[r][c] = '#';
        backtrack(board, r + 1, c, node);
        backtrack(board, r - 1, c, node);
        backtrack(board, r, c + 1, node);
        backtrack(board, r, c - 1, node);
        board[r][c] = ch;
    }
}
