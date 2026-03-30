# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, max_v):
            if not root:
                return (max_v, 0)
            
            if root.val >= max_v:
                self.count += 1
            
            max_v = max(root.val, max_v)

            dfs(root.left, max_v)
            dfs(root.right, max_v)
        
        dfs(root, root.val)
        return self.count