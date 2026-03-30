# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # Do BFS. Create a deque of tuples containing the node, low val, and high val.
        # iterate while there are nodes in the deque. If the node's value is greater
        # than low and lower than high, the tree is valid, otherwise it is invalid.
        q = deque([(root, float('-inf'), float('inf'))])

        while q:
            for _ in range(len(q)):
                node, low, high = q.popleft()
                if node:
                    if not low < node.val < high:
                        return False 
                    # Update your new low and high. If going left, that node
                    # must be lower than the current node and greater than the node
                    # when you last went right (so it should remain "high"). Vice
                    # versa if you go right.
                    q.append((node.left, low, node.val))
                    q.append((node.right, node.val, high))
        return True
                
