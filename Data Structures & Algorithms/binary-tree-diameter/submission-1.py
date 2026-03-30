# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Init solution class with self.res = 0 to keep a global max wrt the class
    def __init__(self):
        self.res = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Need to create a dfs function and see that we need to calculate
        # the diameter at every node which is simply leftDepth + rightDepth,
        # then keep a global total of the maximum.

        def dfs(root):
            if not root:
                return 0
            
            leftDepth = dfs(root.left)
            rightDepth = dfs(root.right)
    
            # Update res with max diamter
            self.res = max(self.res, leftDepth + rightDepth)
    
            # Height of tree at this part of the recursion
            return 1 + max(leftDepth, rightDepth)

        dfs(root)
        return self.res