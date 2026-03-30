"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node_map = {}
        node_map[None] = None
        # curr = head
        # while curr:
        #     node_map[curr] = Node(curr.val, None, None)
        #     curr = curr.next
        
        curr = head
        while curr:
            node_map.setdefault(curr, Node(curr.val)).val = curr.val
            node_map[curr].next = node_map.setdefault(curr.next, Node(0))
            node_map[curr].random = node_map.setdefault(curr.random, Node(0))
            curr = curr.next
        
        return node_map[head] if head else None