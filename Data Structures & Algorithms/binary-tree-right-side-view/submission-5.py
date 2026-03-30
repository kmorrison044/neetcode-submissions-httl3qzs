# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS is most natural. Just create a deque that holds the nodes at each level.
        # Then as you are processing just keep the right most node and append to res
        rsv = []
        q = deque([root])

        while q:
            right = None
            qLen = len(q)
            for _ in range(qLen):
                node = q.popleft()
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            if right:
                rsv.append(right.val)
        return rsv


