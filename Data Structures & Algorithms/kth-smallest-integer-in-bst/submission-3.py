# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0
        self.res = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Do an inorder traversal of the tree and keep going until
        # you hit k.
        def dfs(root, k) -> None: 
            if not root:
                return
    
            self.kthSmallest(root.left, k)
            self.count += 1
            if self.count == k:
                self.res = root.val
                return
            self.kthSmallest(root.right, k)

        dfs(root, k)
        return self.res