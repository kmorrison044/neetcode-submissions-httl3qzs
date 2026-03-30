/*
Definition for a Node.
class Node {
    public int val;
    public List<Node> neighbors;
    public Node() {
        val = 0;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val) {
        val = _val;
        neighbors = new ArrayList<Node>();
    }
    public Node(int _val, ArrayList<Node> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
}
*/

class Solution {
    // Create a HashMap to map orignal nodes to copies,
    // so that we can get copies later to add to a copy's
    // neighbor.
    private Map<Node, Node> oldToNew = new HashMap<>();

    public Node cloneGraph(Node node) {
        // Initial node could be null, run dfs or return null.
        if (node != null)
        {
            return dfs(node);
        }
        return null;
    }

    public Node dfs(Node node)
    {
        // Check if node is already in hashmap, if so, go ahead
        // and return the copy.
        if (oldToNew.containsKey(node)) {
            return oldToNew.get(node);
        }

        // Create a copy with the node's val, add it to
        // the hashmap.
        Node copy = new Node(node.val);
        oldToNew.put(node, copy);

        // Loop over the neighbors in the node,
        // add neighbors to the copy by running dfs on the node.
        for (Node n : node.neighbors) {
            copy.neighbors.add(dfs(n));
        }

        // return the copy for the loop above in another part of the stack.
        return copy;
    }
}