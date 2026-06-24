class UnionFind:
    
    def __init__(self, n: int):
        # Creates parent list. Initialize each node as it's own parent.
        self.parent = [i for i in range(n)]
        # Creates size list for depth of tree
        self.size = [1] * n
        # Tracks number of components. Initially, each node is it's own component.
        # After successfull union operations, we will decrement this number to keep
        # track of the number of components.
        self.n = n

    def find(self, x: int) -> int:
        # Keep recursively calling the find operation while the node is not
        # its own parent. Once we hit the parent node, the recursion will unwind and
        # set the parent of each element called during the recursion to be the
        # root node for faster future calls. This is called "path compression".
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])

        # Return the parent (which is now the root node)
        return self.parent[x]

    def isSameComponent(self, x: int, y: int) -> bool:
        # If two nodes have the same root, then they are apart of the same
        # component.
        return self.find(x) == self.find(y)

    def union(self, x: int, y: int) -> bool:
        # Grab the root's of each node
        root_x = self.find(x)
        root_y = self.find(y)
        # If they have the same root, then they are apart of the same
        # component, thus we can't join them; return False
        if root_x == root_y:
            return False

        # If they are not apart of the same component, then we will join them
        # together by rank ("union by rank"). This will make the tree more balanced,
        # and thus make future find operations quicker, since it traverses less nodes.
        if self.size[root_x] < self.size[root_y]:
            root_y, root_x = root_x, root_y
        if self.size[root_x] == self.size[root_y]:
            # Only increase the size by 1 if both root's have equal size, since we
            # have to add one node to another node. If they aren't the same size, then
            # the child we are adding to the parent won't increase the size, since the
            # parent was already bigger than what the child was.
            self.size[root_x] += 1
        # Set the child to the parent
        self.parent[root_y] = root_x
        # Since we joined to components together, we reduced the total number of 
        # components by 1
        self.n -= 1
        # Return True for successful union
        return True

    def getNumComponents(self) -> int:
        # Since we kept track of the number of components each time we made a successful 
        # union, just return self.n.
        return self.n