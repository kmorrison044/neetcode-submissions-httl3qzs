# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Simple algo to swap the pointers at each node in a DFS fashion.
        if not root: return None # Base case

        root.left, root.right = root.right, root.left # Swap pointers

        # Recurse down tree
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Return root
        return root