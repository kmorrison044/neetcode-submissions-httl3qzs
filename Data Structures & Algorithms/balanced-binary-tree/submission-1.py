# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Init class with _isBalanced var to keep track if the tree is balanced
    def __init__(self):
        self._isBalanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Create dfs function to compute depths at every node
        def dfs(curr):
            if not curr:
                return 0
            
            leftDepth = dfs(curr.left)
            rightDepth = dfs(curr.right)

            # If the left and right subtrees differ in depth > 1, set
            # _isBalanced to False
            if abs(leftDepth - rightDepth) > 1:
                self._isBalanced = False
            
            # Return the depth at the current node
            return 1 + max(leftDepth, rightDepth)
            
        dfs(root)
        return self._isBalanced