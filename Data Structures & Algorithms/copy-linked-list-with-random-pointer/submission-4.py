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
        # Trick is to create a dictionary of original nodes mapped to copied nodes
        # Ensure to create a None: None mapped key to handle an empty linked list or
        # random properties pointing to null.
        # Use setdefault to return the dictionaries' val for that key, or create
        # the key with a specific value. For the next and random sets,
        # create the node with the setdefault function if it doesn't exist in the dictionary
        # then once it reaches that node in the loop, it will automatically udpate the val.
        node_map = {}
        node_map[None] = None
        
        curr = head
        while curr:
            node_map.setdefault(curr, Node(curr.val)).val = curr.val
            node_map[curr].next = node_map.setdefault(curr.next, Node(0))
            node_map[curr].random = node_map.setdefault(curr.random, Node(0))
            curr = curr.next
        
        return node_map[head]