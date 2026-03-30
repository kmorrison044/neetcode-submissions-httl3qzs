# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.mps = float("-inf")
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0
            
            # Run dfs recursively to find left and right, negate negative contributions
            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)
            
            # Adjust mps
            current_path_sum = node.val + left + right
            self.mps = max(self.mps, current_path_sum)
            
            # Return the maximum current path to the parent
            return node.val + max(left, right)
            
        
        dfs(root)
        return self.mps
