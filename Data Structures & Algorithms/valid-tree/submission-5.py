class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Initialize HashMap that stores node : neighbor pairs and
        # a HashSet that stores nodes that have been visited
        # A valid tree is a fully connected, non-cyclical graph.
        adj = {node: [] for node in range(n)}
        visited = set()

        # Append neighbors together the potential tree is undirected
        # so append both ways
        for node, nei in edges:
            adj[node].append(nei)
            adj[nei].append(node)

        # Create a dfs. Params are the current node and it's parent
        def dfs(node, par):
            # If node is already been visited, 
            # we are in a cycle - return false
            if node in visited:
                return False

            visited.add(node)
            # Loop through the neighbors at the current node
            for nei in adj[node]:
                # Ignore if the neighbor is the parent, since
                # it is undirected
                if nei == par:
                    continue
                # Run dfs on the neighbor and pass the current node as the parent.
                # If this returns false, we are in a cycle - return false
                if not dfs(nei, node):
                    return False

            # If it passes the loop, return true
            return True
        
        # Run dfs starting at node 0 with a fake parent (-1).
        # if it is true, there are no cycles and if we visited all nodes, 
        # then it is fully connected and thus a valid tree. Otherwise,
        # it is not a tree.
        return dfs(0, -1) and len(visited) == n