"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            # Return copy if node exists in dict
            if node in oldToNew:
                return oldToNew[node]

            # Otherwise create a new copy with the node's val, add to dict
            # and run through a loop to append neighbors to the copy's 
            # neighbor list. Append neighbors via running dfs on the node
            # in the list.
            copy = Node(node.val)
            oldToNew[node] = copy
            for n in node.neighbors:
                copy.neighbors.append(dfs(n))

            # Return the copy if out of the loop for function earlier in the stack.
            return copy
            
        return dfs(node) if node else None