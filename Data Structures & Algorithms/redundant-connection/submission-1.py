class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # Since there is only 1 cycle num_edges == num_nodes
        n = len(edges)
        # Keep track of the nodes in the cycle and the node
        # That started the cycle
        cycle = set()
        cycleStart = -1
        # Keep track of nodes visited to detect cycle
        visited = set()
        adj = {node: [] for node in range(n + 1)}

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node, par):
            nonlocal cycleStart

            # If node has already been visited, then
            # a cycle has begun. Set cycleStart to the curr
            # node. Return true to flag cycle
            if node in visited:
                cycleStart = node
                return True
            
            visited.add(node)
            for nei in adj[node]:
                # Skip parent since the graph is
                # undirected
                if nei == par:
                    continue
                
                # If we found a cycle, then all of the nodes in
                # the cycle are in the recursion stack, however, not
                # all nodes in the recursion stack are in the cycle.
                # Once we hit the node that is the cycleStart, then 
                # the cycle has ended, so set cycleStart back to -1.
                # If cycleStart is not -1 we are in the cycle, so add node
                # to cycle.
                if dfs(nei, node):
                    if cycleStart != -1:
                        cycle.add(node)
                    if node == cycleStart:
                        cycleStart = -1
                    return True

            return False
        
        # nodes start at 1 in this problem
        dfs(1, -1)
        # Since they want us to return the last edge in the list that
        # is in the cycle, iterate backwards through the list
        for i in range(n-1, -1, -1):
            u, v = edges[i]
            # if both nodes are in the cycle, return this pair.
            if u in cycle and v in cycle:
                return [u, v]

