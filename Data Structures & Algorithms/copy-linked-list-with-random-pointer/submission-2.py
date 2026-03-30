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
        # node_map = {}
        # curr = head
        # while curr:
        #     node_map[curr] = Node(curr.val, None, None)
        #     curr = curr.next
        
        # curr = head
        # while curr:
        #     node_map[curr].next = node_map.get(curr.next)
        #     node_map[curr].random = node_map.get(curr.random)
        #     curr = curr.next
        
        # return node_map[head] if head else None
        oldToCopy = {None: None}

        cur = head
        while cur:
            copy = Node(cur.val)
            oldToCopy[cur] = copy
            cur = cur.next
        cur = head
        while cur:
            copy = oldToCopy[cur]
            copy.next = oldToCopy[cur.next]
            copy.random = oldToCopy[cur.random]
            cur = cur.next
        return oldToCopy[head]

