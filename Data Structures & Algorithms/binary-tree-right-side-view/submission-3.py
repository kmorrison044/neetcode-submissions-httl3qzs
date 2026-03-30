# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.rsv = []
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque([root])

        while q:
            qLen = len(q)
            level = []
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    level.append(node.val)
                
            if level:
                self.rsv.append(level.pop())
                
        return self.rsv


