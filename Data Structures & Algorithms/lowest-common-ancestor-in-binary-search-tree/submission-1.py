# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Not to bad of a problem. A BST is where each node's left and right
        # pointer values are less than and greater than the node's value, respectively.
        # With that in mind, we simply traverse the tree down while both
        # target nodes are either strictly greater than or less than the curr nodes value.
        # when they are not strictly less than or greater than, this means that a
        # split has occurred and you have found the lowest common ancestor.
        while root:
            if min(p.val, q.val) > root.val:
                root = root.right
            elif max(p.val, q.val) < root.val:
                root = root.left
            else:
                return root