class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        # Build adjacency list, since it is undirected, connect nodes
        # both ways
        for u, v, w in edges:
            adj.setdefault(u, []).append([w, v])
            adj.setdefault(v, []).append([w, u])
        
        # This algorithm starts at an arbitrary node, just choose the first node
        # to insert into the heap.
        q = [[0, 0]]
        res = 0
        # Initialize the visit set.
        visit = set()
        while q and len(visit) < n:
            # Pop the weight and node
            weight, node = heapq.heappop(q)

            # If this node has already been visited, skip processing it
            if node in visit:
                continue
            
            # Add the weight of this node and mark it as visited
            res += weight
            visit.add(node)

            # Loop through all of the neighbors, check if they have been visited.
            # if not add the node and weight to the heap.
            for w, nei in adj.get(node, []):
                if nei not in visit:
                    heapq.heappush(q, [w, nei])
        
        # Return the result if we visited each node. If we didn't visit all nodes,
        # this means that the graph was not connected, so return -1 per the requirement.
        return res if len(visit) == n else -1