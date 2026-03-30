class TrieNode {
    HashMap<Character, TrieNode> children;
    boolean isLeaf;

    public TrieNode() {
        children = new HashMap<>();
        isLeaf = false;
    }

    public void insert(String word) {
        TrieNode curr = this;
        for (char c : word.toCharArray()) {
            curr.children.putIfAbsent(c, new TrieNode());
            curr = curr.children.get(c);
        }
        curr.isLeaf = true;
    }
}

class Solution {
    private Set<String> res;
    List<Character> curr = new ArrayList<>();

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
        StringBuilder sb = new StringBuilder();
        int ROWS = board.length, COLS = board[0].length;

        if (r < 0 || c < 0 || r >= ROWS || c >= COLS ||
            board[r][c] == '#' || !node.children.containsKey(board[r][c])) {
                return;
            }

        char ch = board[r][c]; 
        curr.add(ch);
        node = node.children.get(board[r][c]);
        board[r][c] = '#';
        if (node.isLeaf) {
            for (Character cht : curr) {
                sb.append(cht);
            }
            res.add(sb.toString());
        }

        backtrack(board, r + 1, c, node);
        backtrack(board, r - 1, c, node);
        backtrack(board, r, c + 1, node);
        backtrack(board, r, c - 1, node);
        curr.remove(curr.size() - 1);
        board[r][c] = ch;
    }
}
