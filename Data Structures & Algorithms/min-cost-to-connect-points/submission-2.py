class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Prim's algorithm for finding a Minimum Spanning Tree
        
        # Define function to find edge weight
        def manhat(a, b):
            return abs(a[0] - b[0]) + abs(a[1] - b[1])
        
        n = len(points)
        adj = {}
        # Create adjacency list. Nodes will be considered the index
        # of the points list.
        for i in range(n):
            # Only iterate through i + 1 to n - 1 since we are creating
            # both directional edges at the same time. This also means
            # we are calling the manhat function once.
            for j in range(i + 1, n):
                dist = manhat(points[i], points[j])
                adj.setdefault(i, []).append([dist, j])
                adj.setdefault(j, []).append([dist, i])
        
        # Start at an arbitrary vertex (vertex 0)
        q = [[0, 0]]
        # This will keep track of the total weight of all edges in the minimum
        # spanning tree.
        res = 0
        # Initialize visit set to ensure we are keeping track of nodes we
        # have already seen.
        visit = set()

        # Iterate until the q is empty or we visited every node.
        while q and len(visit) < n:
            # Grab the minimum weight and point
            weight, point = heapq.heappop(q)

            # If we already visited this node, skip processing it again.
            if point in visit:
                continue
            
            # We are processing this node, so add it's edge weight to the total
            # edge weight of the MST
            res += weight
            # Mark this node as visited
            visit.add(point)

            # Grab the weight and neighbors of the current node via the adj list.
            for w, nei in adj.get(point, []):
                # If we haven't visited the neighbor yet, add it to the min heap so that
                # we can keep grabbing the node with the least weight.
                if nei not in visit:
                    heapq.heappush(q, [w, nei])
        
        # Return the result.
        return res