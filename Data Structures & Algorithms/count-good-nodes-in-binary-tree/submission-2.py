# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # Use dfs. At every node keep track of the current max_v. If the node.val is
        # greater or equal to the current max_v, the count it as 1, else count 0,
        # then update your max and add the results from the other parts of recursion.
        # if at None, return 0 because it is not a good node.
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