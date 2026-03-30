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
        if not self.head:
            self.head = self.tail = node
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node

    def _touch(self, node: Node):
        if node is self.tail:
            return
        
        self._removeNode(node)
        self._addToTail(node)

    def get(self, key: int) -> int:
        if key in self.cache:
            self._touch(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self._touch(self.cache[key])
            return
        
        self.cache[key] = Node(key, value)
        self._addToTail(self.cache[key])

        if len(self.cache) > self.cap:
            del self.cache[self.head.key]
            self._removeNode(self.head)
