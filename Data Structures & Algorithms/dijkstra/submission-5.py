class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        # Create adj list
        adj = {}
        for u, v, w in edges:
            adj.setdefault(u, []).append((w, v))
        
        # Create shortest list where i is a node and node[i] is
        # the shortest distance to that node
        shortest = [float("inf") for node in range(n)]
        shortest[src] = 0

        # Initialize q with source node and 0 weight to the source node
        q = [(0, src)]
        while q:
            # Pop from the q to get the shortest distance to the node and the node itself
            curr_d, curr_node = heapq.heappop(q)

            # If the current distance is greater than what has been previously seen,
            # skip processing this node again
            if curr_d > shortest[curr_node]:
                continue
            
            # Iterate through each neighbor to the current node
            for w, v in adj.get(curr_node, []):
                # calculate the new total distance to get to the next node
                new_d = curr_d + w
                # If this new distance is shorter than what is previously recorded for the 
                # node, then update the shortest distance and push the node to the heap.
                if new_d < shortest[v]:
                    shortest[v] = new_d
                    heapq.heappush(q, (new_d, v))
        
        # Do some python to return it in the form of a hashmap.
        return {i: v if v != float("inf") else -1 for i, v in enumerate(shortest)}