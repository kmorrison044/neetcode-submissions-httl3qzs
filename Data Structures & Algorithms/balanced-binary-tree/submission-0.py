# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self._isBalanced = True
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr):
            if not curr:
                return 0
            
            leftDepth = dfs(curr.left)
            rightDepth = dfs(curr.right)

            if abs(leftDepth - rightDepth) > 1:
                self._isBalanced = False
            
            return 1 + max(leftDepth, rightDepth)
            
        dfs(root)
        return self._isBalanced