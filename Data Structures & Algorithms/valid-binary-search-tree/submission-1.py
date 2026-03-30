# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            for _ in range(len(q)):
                node, low, high = q.popleft()
                if node:
                    if not low < node.val < high:
                        return False 
                    q.append((node.left, low, node.val))
                    q.append((node.right, node.val, high))
        return True
                
