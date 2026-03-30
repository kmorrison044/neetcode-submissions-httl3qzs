# We solve this problem by having a dictionary where the key is the given key
# and the value is a node in a linked list. The linked list keeps track of
# the LRU and MRU keys. It a get or put operation is applied to a key, then
# we will move that node to the tail of the doubly-linked list, making it the
# MRU. So the get operation will look up the node in the dictionary and return
# the value of the node. The put operation will add the key with the node to
# the dictionary, and add it to the end of the list. If the key already exists,
# we remove the node from its spot, update its value, and append it to the end
# of the list. If the size of the dictionary is greater than the capacity,
# we remove the LRU by grabbing the head of the list and deleting it from the
# list and the key from the dictionary.
class Node:
    def __init__(self, key: int = None, val: int = None):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head, self.tail = None, None

    def _removeNode(self, node: Node):
        # To remove a node, check if the prev and next attributes have values
        # then change the pointers to the previous and next nodes. If they don't 
        # have values, then that means the node was the head or tail of the list,
        # so we update the head and tail accordingly. Finally, the change the nodes
        # pointers to None to delete it.
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        node.prev = node.next = None
        
    def _addToTail(self, node: Node):
        # If head is None, then no nodes have been added to the list yet.
        # set head and tail to the node and return.
        if not self.head:
            self.head = self.tail = node
            return
        
        # Put the node to the end of the list by setting it's "prev" pointer 
        # to the tail, setting the "next" pointer of the current tail to the node
        # and then moving the tail to the node.
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def _touch(self, node: Node):
        # This function updates a node whenever it has operations performed on it.
        # if the node is already the tail, we don't have to update anything.
        if node is self.tail:
            return
        
        # If the node is not already the tail, delete it from it's current position
        # and then add it to the tail.
        self._removeNode(node)
        self._addToTail(node)

    def get(self, key: int) -> int:
        # If the key is in the cache, update the node to the MRU and return
        # its value, otherwise return -1
        if key in self.cache:
            self._touch(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # If key is in the cache, update the node to the new value by looking it up
        # in the dict, then add it to the MRU.
        if key in self.cache:
            self.cache[key].val = value
            self._touch(self.cache[key])
            return
        
        # If it doesn't already exist in the dictionary, create a new node and add it
        # to the dictionary, then add it as the tail of the linked list.
        self.cache[key] = Node(key, value)
        self._addToTail(self.cache[key])

        # if the cache exceeds capacity, then delete it from the cache and linked list.
        if len(self.cache) > self.cap:
            del self.cache[self.head.key]
            self._removeNode(self.head)
