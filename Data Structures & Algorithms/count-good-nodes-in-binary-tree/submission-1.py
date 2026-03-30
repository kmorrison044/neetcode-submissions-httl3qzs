# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_v):
            if not root:
                return 0
            
            if root.val >= max_v:
                res = 1
            else:
                res = 0
            
            max_v = max(root.val, max_v)

            res += dfs(root.left, max_v)
            res += dfs(root.right, max_v)
            return res
        
        return dfs(root, root.val)