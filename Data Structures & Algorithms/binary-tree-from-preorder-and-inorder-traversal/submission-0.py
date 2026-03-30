# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.preIdx = 0
        self.inIdx = 0
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(limit):
            if self.preIdx >= len(preorder):
                # No more nodes
                return None
            if inorder[self.inIdx] == limit:
                # Subtree complete
                self.inIdx += 1
                return None
            
            root = TreeNode(preorder[self.preIdx]) # Create node
            self.preIdx += 1 # Increment preorder
            root.left = dfs(root.val) # The left limit is curr node
            root.right = dfs(limit) # Right limit is inherited from parent
            return root
        return dfs(float('inf'))
        