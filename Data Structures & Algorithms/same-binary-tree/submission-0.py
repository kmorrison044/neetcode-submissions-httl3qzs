# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.isSame = True
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(q, p):
            if q == None or p == None:
                if p != q:
                    self.isSame = False
                return

            if p and q and p.val != q.val:
                self.isSame = False
                return
            
            if not self.isSame:
                return

            dfs(q.left, p.left)
            dfs(q.right, p.right)

        dfs(p, q)
        return self.isSame

            